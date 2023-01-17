import os
from stockapi import vault


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess-if-you-can'

    url = "https://yh-finance.p.rapidapi.com/market/get-trending-tickers"
    apihost = 'yh-finance.p.rapidapi.com'
    apikey = '1d339fb931msh3da01e6574dd13fp190cddjsnd38ed93cdaa4'
    FMP_apiKey = "?apikey=20f6b9477a4df6684cb7a71ee4e80274"
    news_url = "https://yh-finance.p.rapidapi.com/news/v2/get-details"
    post_news_url = "https://yh-finance.p.rapidapi.com/news/v2/list"
    recommendation_url = "https://yh-finance.p.rapidapi.com/stock/v2/get-recommendations"
    chart_url = "https://yh-finance.p.rapidapi.com/stock/v2/get-chart"
    insight_url = "https://yh-finance.p.rapidapi.com/stock/v2/get-insights"
    gainers_url = "https://financialmodelingprep.com/api/v3/stock/gainers" + FMP_apiKey
    losers_url = "https://financialmodelingprep.com/api/v3/stock/losers" + FMP_apiKey
    marketHours_url = "https://financialmodelingprep.com/api/v3/is-the-market-open" + FMP_apiKey
    stockRating_url = "https://financialmodelingprep.com/api/v3/rating/"
    sectorPerformance_url = "https://financialmodelingprep.com/api/v3/stock/sectors-performance" + FMP_apiKey

    headers = {
        'x-rapidapi-host': apihost,
        'x-rapidapi-key': apikey
    }

    PROJECT_NAME = "WallStreet"
    GOOGLE_CLIENT_ID = vault.GOOGLE_CLIENT_ID
    GOOGLE_CLIENT_SECRET = vault.GOOGLE_CLIENT_SECRET
    GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")

    # db credentials
    db_host = vault.dbhost
    db_database = vault.database
    db_username = vault.username
    db_password = vault.password

