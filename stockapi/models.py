from . import db


# create Table stockinfo
class stockinfo(db.Model):
    symbol = db.Column(db.String(10), primary_key=True)
    industry = db.Column(db.String(250))
    revenueGrowth = db.Column(db.Numeric(12, 2), nullable=True)
    targetLowPrice = db.Column(db.Numeric(12, 2), nullable=True)
    targetHighPrice = db.Column(db.Numeric(12, 2), nullable=True)
    recommendationKey = db.Column(db.String(30), nullable=True)
    grossProfits = db.Column(db.BigInteger(), nullable=True)
    currentPrice = db.Column(db.Numeric(12, 2), nullable=True)
    numberOfAnalystOpinions = db.Column(db.Integer(), nullable=True)
    totalRevenue = db.Column(db.BigInteger(), nullable=True)
    heldPercentInstitutions = db.Column(db.Numeric(10, 2), nullable=True)
    shortRatio = db.Column(db.Numeric(10, 2), nullable=True)
    beta = db.Column(db.Numeric(10, 2), nullable=True)
    regularMarketDayHigh = db.Column(db.Numeric(10, 2), nullable=True)
    regularMarketDayLow = db.Column(db.Numeric(10, 2), nullable=True)
    regularMarketVolume = db.Column(db.BigInteger(), nullable=True)
    marketCap = db.Column(db.BigInteger(), nullable=True)
    fiftyTwoWeekHigh = db.Column(db.Numeric(10, 2), nullable=True)
    fiftyTwoWeekLow = db.Column(db.Numeric(10, 2), nullable=True)
    dividendYield = db.Column(db.Numeric(10, 2), nullable=True)

    def __init__(self, symbol, industry, revenueGrowth, targetLowPrice,
                 targetHighPrice, recommendationKey, grossProfits, currentPrice, numberOfAnalystOpinions,
                 totalRevenue, heldPercentInstitutions, shortRatio, beta, regularMarketDayHigh, regularMarketDayLow,
                 regularMarketVolume, marketCap, fiftyTwoWeekHigh, fiftyTwoWeekLow, dividendYield):
        self.symbol = symbol
        self.industry = industry
        self.revenueGrowth = revenueGrowth
        self.targetLowPrice = targetLowPrice
        self.targetHighPrice = targetHighPrice
        self.recommendationKey = recommendationKey
        self.grossProfits = grossProfits
        self.currentPrice = currentPrice
        self.numberOfAnalystOpinions = numberOfAnalystOpinions
        self.totalRevenue = totalRevenue
        self.heldPercentInstitutions = heldPercentInstitutions
        self.shortRatio = shortRatio
        self.beta = beta
        self.regularMarketDayHigh = regularMarketDayHigh
        self.regularMarketDayLow = regularMarketDayLow
        self.regularMarketVolume = regularMarketVolume
        self.marketCap = marketCap
        self.fiftyTwoWeekHigh = fiftyTwoWeekHigh
        self.fiftyTwoWeekLow = fiftyTwoWeekLow
        self.dividendYield = dividendYield


