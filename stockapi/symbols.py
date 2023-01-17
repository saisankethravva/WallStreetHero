class Tickers:
    def __init__(self, quote):
        self.industry = quote.info['industry']
        self.revenueGrowth = quote.info['revenueGrowth'] * 100
        self.targetLowPrice = quote.info['targetLowPrice']
        self.targetHighPrice = quote.info['targetHighPrice']
        self.recommendationKey = quote.info['recommendationKey']
        self.grossProfits = quote.info['grossProfits']
        self.currentPrice = quote.info['currentPrice']
        self.numberOfAnalystOpinions = quote.info['numberOfAnalystOpinions']
        self.totalRevenue = quote.info['totalRevenue']
        self.heldPercentInstitutions = quote.info['heldPercentInstitutions']
        self.shortRatio = quote.info['shortRatio']
        self.beta = quote.info['beta']
        self.regularMarketDayHigh = quote.info['regularMarketDayHigh']
        self.averageVolume10days = quote.info['averageVolume10days']
        self.regularMarketDayLow = quote.info['regularMarketDayLow']
        self.regularMarketVolume = quote.info['regularMarketVolume']
        self.marketCap = quote.info['marketCap']
        self.fiftyTwoWeekHigh = quote.info['fiftyTwoWeekHigh']
        self.fiftyTwoWeekLow = quote.info['fiftyTwoWeekLow']
        self.dividendYield = quote.info['dividendYield']


class Summary:
    @staticmethod
    def to_dict(stock_info_db):
        my_dict = {"industry": stock_info_db.industry,
                   "currentPrice": str(stock_info_db.currentPrice),
                   "52TwoWeekLow": str(stock_info_db.fiftyTwoWeekLow),
                   "52TwoWeekHigh": str(stock_info_db.fiftyTwoWeekHigh),
                   "MarketDayHigh": str(stock_info_db.regularMarketDayHigh),
                   "targetLowPrice": str(stock_info_db.targetLowPrice),
                   "targetHighPrice": str(stock_info_db.targetHighPrice),
                   "dividend": str(stock_info_db.dividendYield),
                   "Volume": str(stock_info_db.regularMarketVolume),
                   "MarketCap": str(stock_info_db.marketCap),
                   "recommendation": stock_info_db.recommendationKey,
                   "TotalRevenue": str(stock_info_db.totalRevenue)
                   }
        return my_dict


class Charts:
    @staticmethod
    def create_charts(my_dict):
        charts_dict = {"symbol": my_dict['symbol'],
                       "chartPreviousClose": my_dict['chartPreviousClose'],
                       "currency": my_dict['currency'],
                       "exchangeName": my_dict['exchangeName'],
                       "exchangeTimezoneName": my_dict['exchangeTimezoneName'],
                       "firstTradeDate": my_dict['firstTradeDate'],
                       "instrumentType": my_dict['instrumentType'],
                       "previousClose": my_dict['previousClose'],
                       "regularMarketPrice": my_dict['regularMarketPrice'],
                       "regularMarketTime": my_dict['regularMarketTime'],
                       "scale": my_dict['scale'],
                       "timezone": my_dict['timezone']
                       }
        return charts_dict


class CInsight:
    @staticmethod
    def get_insight(comp_dict):
        comp_dict = {"symbol": comp_dict['symbol'],
                     "valuation": comp_dict['instrumentInfo']['valuation']['description'],
                     "summary": comp_dict['reports'][0]['summary'],
                     "companySnapshot": str(comp_dict['companySnapshot']['sectorInfo']),
                     "earningsReports": str(comp_dict['companySnapshot']['company']['earningsReports'])
                     }
        return comp_dict


class Rating:
    @staticmethod
    def rating(response):

        stockRating = {"Symbol": response[0]["symbol"], "Grade": response[0]["rating"],
                       "Recommendation": response[0]["ratingRecommendation"]}
        return stockRating
