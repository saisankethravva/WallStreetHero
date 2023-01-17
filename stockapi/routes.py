from . import db, app
from flask import Blueprint, request, jsonify, redirect, url_for, json
import yfinance as yf
from stockapi.models import stockinfo
from sqlalchemy import inspect
from sqlalchemy import create_engine
from stockapi.symbols import Tickers, Summary, Charts, CInsight, Rating
from stockapi import vault
from bs4 import BeautifulSoup
from flask_login import (
    LoginManager,
    current_user,
    login_required
)
from oauthlib.oauth2 import WebApplicationClient
# Python standard libraries
import json
import os
from stockapi.config import Config
from stockapi import psqlprovider
from stockapi.jwt_helper import decode_jwt_token, encode_jwt_token
from stockapi.user import User
import requests

# Configuration
GOOGLE_CLIENT_ID = Config.GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = Config.GOOGLE_CLIENT_SECRET
GOOGLE_DISCOVERY_URL = Config.GOOGLE_DISCOVERY_URL

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# OAuth 2 client1 setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

stock_api_blueprint = Blueprint("stockapi", __name__)

engine = create_engine(
    'postgresql://' + vault.username + ':' + vault.password + '@' + vault.dbhost + '/' + vault.database)
inspector = inspect(engine)


# add try and except
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@stock_api_blueprint.route('/', methods=['GET'])
@stock_api_blueprint.route('/home', methods=['GET'])
def get_home_page():
    try:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200
    except:
        return jsonify({"Message": "Home page is unreachable"}), 400


# # Used for debugging only
# @stock_api_blueprint.route("/")
# def index():
#     if current_user != None and current_user.is_authenticated:
#         return (
#             "<p>Hello, {}! You're logged in! Email: {}</p>"
#             "<div><p>Google Profile Picture:</p>"
#             '<img src="{}" alt="Google profile pic"></img></div>'
#             '<a class="button" href="/logout">Logout</a>'.format(
#                 current_user.name, current_user.email, current_user.profile_pic
#             )
#         )
#     else:
#         return '<a class="button" href="/google_login">Google Login</a>'

# Add stock summary to DB(internal call) just to add tickers to DB

# implement a small functionality on UI for admins to enter the ticker and this call will enter the symbol to DB.


@stock_api_blueprint.route('/add_ticker', methods=['GET', 'POST'])
def add_ticker():
    if request.method == 'POST':
        # Read the symbol from the frontend app.(admin work)

        symbol = request.json['symbol']
        quote = yf.Ticker(symbol)
        tickers = Tickers(quote)
        stock_object = stockinfo(symbol, tickers.industry, tickers.revenueGrowth, tickers.targetLowPrice,
                                 tickers.targetHighPrice, tickers.recommendationKey, tickers.grossProfits,
                                 tickers.currentPrice, tickers.numberOfAnalystOpinions, tickers.totalRevenue,
                                 tickers.heldPercentInstitutions, tickers.shortRatio, tickers.beta,
                                 tickers.regularMarketDayHigh, tickers.regularMarketDayLow, tickers.regularMarketVolume,
                                 tickers.marketCap, tickers.fiftyTwoWeekHigh, tickers.fiftyTwoWeekLow,
                                 tickers.dividendYield)
        # adding data to stockinfo table
        if inspector.has_table(stockinfo.__name__):
            db.session.add(stock_object)
            db.session.commit()
            db.session.flush()
        else:
            db.create_all()
            db.session.add(stock_object)
            db.session.commit()
            db.session.flush()

        return jsonify({"symbol": symbol,
                        "Message": "successfully added" + ' ' + symbol + ' ' + '.'
                        }), 200


@stock_api_blueprint.route('/update_ticker', methods=['GET', 'POST'])
def update_ticker():
    try:
        if request.method == 'POST':
            # Read the symbol from the frontend app.(admin work)

            symbol = request.json['symbol']
            quote = yf.Ticker(symbol)
            tickers = Tickers(quote)
            db_object = stockinfo.query.filter_by(symbol=symbol).first()
            stock_object = stockinfo(symbol, tickers.industry, tickers.revenueGrowth, tickers.targetLowPrice,
                                     tickers.targetHighPrice, tickers.recommendationKey, tickers.grossProfits,
                                     tickers.currentPrice, tickers.numberOfAnalystOpinions, tickers.totalRevenue,
                                     tickers.heldPercentInstitutions, tickers.shortRatio, tickers.beta,
                                     tickers.regularMarketDayHigh, tickers.regularMarketDayLow,
                                     tickers.regularMarketVolume,
                                     tickers.marketCap, tickers.fiftyTwoWeekHigh, tickers.fiftyTwoWeekLow,
                                     tickers.dividendYield)

            # update feilds in DB.
            db_object.targetLowPrice = stock_object.targetLowPrice
            db_object.targetHighPrice = stock_object.targetHighPrice
            db_object.recommendationKey = stock_object.recommendationKey
            db_object.currentPrice = stock_object.currentPrice
            db_object.totalRevenue = stock_object.totalRevenue
            db_object.regularMarketDayHigh = stock_object.regularMarketDayHigh
            db_object.regularMarketDayLow = stock_object.regularMarketDayLow
            db_object.fiftyTwoWeekHigh = stock_object.fiftyTwoWeekHigh
            db_object.fiftyTwoWeekLow = stock_object.fiftyTwoWeekLow
            db.session.commit()
            return jsonify({"symbol": symbol,
                            "message": "Updated successfully" + ' ' + symbol + ' ' + '.'
                            }), 200

    except:
        return jsonify({"symbol": symbol,
                        "message": "Symbol not added" + ' ' + symbol + ' ' + '.'
                        }), 400
    else:
        return jsonify({"message": "welcome to wall street home page"}), 200


# API endpoint to fetch ticker info from DB and show on the UI on Popup

@stock_api_blueprint.route('/stock/info', methods=['GET', 'POST'])
def get_stock_info():
    if request.method == 'POST':
        # Read the symbol from the frontend app.
        try:
            symbol = request.json['symbol']
            stock_info_db = stockinfo.query.filter_by(symbol=symbol).first()
            my_dict = Summary.to_dict(stock_info_db)
            return jsonify(my_dict), 200
        except:
            return jsonify({"Message": "Cannot retrieve stock info at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# trending tickers based on user selection
@stock_api_blueprint.route('/trending/tickers', methods=['GET'])
def get_trending_ticker():
    if request.method == 'GET':
        try:
            # selection = request.json['selection']
            # top_n = int(selection)
            url = Config.url
            querystring = {"region": "US"}
            response = requests.request("GET", url, headers=Config.headers, params=querystring)
            my_dict = response.json()
            trending_list = my_dict['finance']['result'][0]['quotes']

            # trending_tickers = {}
            trending_tickers = []
            for index in range(5):
                # trending_tickers[trending_list[index]["symbol"]] = trending_list[index]["shortName"]
                trending_tickers.append(
                    {"symbol": trending_list[index]["symbol"], "company": trending_list[index]["shortName"]})
            return jsonify(trending_tickers), 200
        except:
            return jsonify(
                {"Message": "Cannot retrieve trending tickers at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# get real time current stock price
@stock_api_blueprint.route('/realtime/stock/price', methods=['GET', 'POST'])
def get_stock_price():
    if request.method == 'POST':
        # Read the symbol from the frontend app.
        try:
            symbol = request.json['symbol']
            quote = yf.Ticker(symbol)
            currentPrice = quote.info['currentPrice']
            return jsonify({
                "currentStockPrice": currentPrice
            }), 200

        except:
            return jsonify({"Message": "Cannot retrieve current stock price"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# get UUId of news
def get_news_uuid():
    try:
        url = Config.post_news_url
        querystring = {"region": "US", "snippetCount": "5"}
        payload = ""
        top_n = 5
        response_list = []
        headers = {
            'content-type': "text/plain",
            'x-rapidapi-host': Config.apihost,
            'x-rapidapi-key': Config.apikey
        }
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        my_dict = response.json()
        for index in range(0, top_n):
            response_list.append(my_dict["data"]["main"]["stream"][index]["id"])
        return response_list
    except:
        return "cannot retrieve UUID's+"


@stock_api_blueprint.route('/news', methods=['GET'])
def get_news():
    try:
        uuid_list = get_news_uuid()
        url = Config.news_url
        # news_dict = {}
        news_dict = []
        counter = 1
        for uuid in uuid_list:
            querystring = {"uuid": uuid, "region": "US"}
            response = requests.request("GET", url, headers=Config.headers, params=querystring)
            data = response.json()
            for item in data["data"]["contents"]:
                if item["content"]["clickThroughUrl"] is None:
                    clickThrough = item["content"]["canonicalUrl"]["url"]
                    # clickThrough = "URL Not available from the news maker"
                else:
                    clickThrough = item["content"]["clickThroughUrl"]["url"]
                title = item["content"]["title"]
                # news_dict[counter] = [title, clickThrough]
                news_dict.append({"title": title, "url": clickThrough})
                counter += 1
        return jsonify(news_dict), 200
    except:
        return jsonify({"Message": "Cannot retrieve news at this time"}), 401


# get similar stocks of a given stock
@stock_api_blueprint.route('/lookalike', methods=['GET', 'POST'])
def get_same_category():
    rec_dict = {}
    if request.method == 'POST':
        try:
            # Enter symbol and get the similar recommendation
            symbol = request.json['symbol']
            url = Config.recommendation_url
            querystring = {"symbol": symbol}
            response = requests.request("GET", url, headers=Config.headers, params=querystring)
            my_dict = response.json()
            recommendation_list = my_dict['finance']['result'][0]['quotes']
            for index in recommendation_list:
                rec_dict[index['shortName'] + '(' + index['symbol'] + ')'] = index["regularMarketPrice"]

            return jsonify(rec_dict), 200
        except:
            return jsonify({"Message": "Cannot retrieve same category stocks at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# get charts of the symbol
@stock_api_blueprint.route('/charts', methods=['GET', 'POST'])
def get_charts():
    if request.method == 'POST':
        try:
            # Enter symbol and get the charts .
            symbol = request.json['symbol']
            url = Config.chart_url
            querystring = {"interval": "5m", "symbol": symbol, "range": "1d", "region": "US"}
            response = requests.request("GET", url, headers=Config.headers, params=querystring)
            data = response.json()
            charts_dict = Charts.create_charts(data['chart']['result'][0]['meta'])
            return jsonify(charts_dict), 200
        except:
            return jsonify({"Message": "Cannot retrieve charts at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# get insight about a company
@stock_api_blueprint.route('/company/insight', methods=['GET', 'POST'])
def get_company_insight():
    if request.method == 'POST':
        try:
            # Enter symbol and get company insight.
            symbol = request.json['symbol']
            url = Config.insight_url
            querystring = {"symbol": symbol}
            response = requests.request("GET", url, headers=Config.headers, params=querystring)
            data = response.json()
            company_dict = CInsight.get_insight(data['finance']['result'])
            return jsonify(company_dict)
        except:
            return jsonify({"Message": "Cannot retrieve company insight at this time"}), 401
    else:
        return jsonify({"message": "welcome to wall street home page"}), 200


@stock_api_blueprint.route("/google_login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(Config.GOOGLE_CLIENT_ID, Config.GOOGLE_CLIENT_SECRET)
    )

    # Parse the tokens!
    token = token_response.json()
    client.parse_request_body_response(json.dumps(token_response.json()))
    # token_temp  = token_response.json()
    # print(token_temp)
    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    client.access_token
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    print(userinfo_response)
    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    user_info = userinfo_response.json()
    if userinfo_response.json().get("email_verified"):
        users_email = userinfo_response.json()["email"]

        # // Get user from db
        user = psqlprovider.get_user(users_email)
        if (user is not None):
            user = User(user['email'], user['fn'], user['ln'], user['user_id'], user['role_id'])
            encoded_token = encode_jwt_token(user);

            return jsonify({"access_token": encoded_token}), 200
        else:
            return jsonify({"access_token": None}), 400
    else:
        return "User email not available or not verified by Google.", 400


def get_jwt_token(request):
    authorization_header_value = request.headers.get('Authorization')
    if (authorization_header_value != None):
        jwt_token = authorization_header_value.split(" ")[1]
        return jwt_token
    else:
        return None


@login_manager.request_loader
def load_user_from_request(request):
    try:
        jwt_token = get_jwt_token(request)
        if (jwt_token != None):
            payload = decode_jwt_token(jwt_token)

            # Get user from db
            user = psqlprovider.get_user(payload["email"])
            user = User(user['email'], user['fn'], user['ln'], user['user_id'], user['role_id'])
            return user
    except os.error as e:
        return None
    return None


@stock_api_blueprint.route("/current-user")
def get_current_user():
    user = psqlprovider.get_user(current_user.get_id())
    return jsonify(user), 200


@stock_api_blueprint.route("/ping")
def ping():
    return "Success", 200


@stock_api_blueprint.route("/login", methods=['POST'])
def login():
    json_data = request.get_json()
    print(json_data)
    user = psqlprovider.verify_user(json_data["username"], json_data["password"])
    if (user is not None):
        user = User(user['email'], user['fn'], user['ln'], user['user_id'], user['role_id'])
        encoded_token = encode_jwt_token(user);
        return jsonify({"access_token": encoded_token}), 200

    else:
        return jsonify({"access_token": None}), 400


@stock_api_blueprint.route("/ping-auth")
@login_required
def pingAuth():
    return "message"


@stock_api_blueprint.route("/user", methods=['POST'])
def create_user():
    json_data = request.get_json()
    message = psqlprovider.add_user(json_data)
    if (message == "Success"):
        return jsonify({"message": message}), 200
    return jsonify({"message": message.pgerror}), 400


@stock_api_blueprint.route("/google_login")
def google_login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


# get the top 5 gainers for the day
@stock_api_blueprint.route('/get-gainers', methods=['GET'])
def get_gainers():
    if request.method == 'GET':
        try:
            gainersDictionary = []
            url = Config.gainers_url
            response = requests.request("GET", url)
            response = response.json()
            for x in range(5):
                gainersDictionary.append({"stock": response["mostGainerStock"][x]["ticker"],
                                          "price": response["mostGainerStock"][x]["price"],
                                          "changes": response["mostGainerStock"][x]["changes"],
                                          "changePercent": response["mostGainerStock"][x]["changesPercentage"]})
            return jsonify(gainersDictionary), 200
        except:
            return jsonify({"Message": "Cannot retrieve top 5 gainers at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# get the top 5 losers for the day
@stock_api_blueprint.route('/get-losers', methods=['GET'])
def get_losers():
    if request.method == 'GET':
        try:
            losersDictionary = []
            url = Config.losers_url
            response = requests.request("GET", url)
            response = response.json()
            for x in range(5):
                losersDictionary.append({"stock": response["mostLoserStock"][x]["ticker"],
                                          "price": response["mostLoserStock"][x]["price"],
                                          "changes": response["mostLoserStock"][x]["changes"],
                                          "changePercent": response["mostLoserStock"][x]["changesPercentage"]})
            return jsonify(losersDictionary), 200
        except:
            return jsonify({"Message": "Cannot retrieve top 5 losers at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# get market open and close times as well as if market is open
@stock_api_blueprint.route('/get-market-hours', methods=['GET'])
def get_market_hours():
    if request.method == 'GET':
        try:
            marketHours = []
            url = Config.marketHours_url
            response = requests.request("GET", url)
            response = response.json()
            marketHours.append({"isMarketOpen": response["isTheStockMarketOpen"],
                                "marketOpenHours": response['stockMarketHours']['openingHour'],
                                "marketCloseHours": response['stockMarketHours']['closingHour']})
            return jsonify(marketHours), 200
        except:
            return jsonify({"Message": "Cannot retrieve market hours at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# get the rating of a stock
@stock_api_blueprint.route('/get-stock-rating', methods=['POST'])
def get_stock_rating():
    if request.method == 'POST':
        try:
            symbol = request.get_json()
            symbol = symbol['search'].upper()
            url = Config.stockRating_url + symbol + Config.FMP_apiKey
            response = requests.request("GET", url)
            response = response.json()
            stockRating = Rating.rating(response)
            return jsonify(stockRating), 200
        except:
            return jsonify({"Message": "Cannot retrieve stock rating at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# get performance metrics of 15 sectors
@stock_api_blueprint.route('/get-sector-performance', methods=['GET'])
def get_sector_performance():
    if request.method == 'GET':
        try:
            sectorPerformance = []
            url = Config.sectorPerformance_url
            response = requests.request("GET", url)
            response = response.json()
            for x in range(14):
                sectorPerformance.append({"sector": response['sectorPerformance'][x]['sector'],
                                          "change": response['sectorPerformance'][x]['changesPercentage']})
            return jsonify(sectorPerformance), 200
        except:
            return jsonify({"Message": "Cannot retrieve sector performance at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200


# Web scraper to scrape GoScour for top 5 most mentioned stock tickers on Reddit within 24 hour period
# Inspired by https://realpython.com/beautiful-soup-web-scraper-python/
@stock_api_blueprint.route('/get-reddit-mentions', methods=['GET'])
def get_reddit_mentions():
    if request.method == 'GET':
        try:
            url = "https://www.goscour.com/"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            mentionedStocks = []

            results = soup.find(id="reddit-stocks-leaderboard")
            stockSymbol = results.find_all("div", class_="font-medium block")
            companyName = results.find_all("div", class_="text-text-secondary dark:text-text-primaryDark")
            # mentionCount = results.find_all("div", class_="px-4 py-4 text-right table-cell align-middle")

            for symbols, names, x in zip(stockSymbol, companyName, range(5)):
                mentionedStocks.append({"symbol": symbols.text, "company": names.text})
            return jsonify(mentionedStocks)
        except:
            return jsonify({"Message": "Cannot retrieve Reddit mentions at this time"}), 401
    else:
        return jsonify({"Message": "Welcome to Wall Street Hero"}), 200
