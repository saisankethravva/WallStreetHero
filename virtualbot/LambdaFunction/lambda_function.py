"""
Demonstrates an implementation of the Lex Code Hook Interface
in order to serve a Wall Street bot which manages stocks and return current stock price.
Bot, Intent, and Slot models which are compatible with this sample can be found in the Lex Console
as part of the 'WallStreet' template.
"""
import logging
from StockHandler import StockAPIHandler;

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """

def get_slots(intent_request):
    return intent_request['currentIntent']['slots']

def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response

""" --- Functions that control the bot's behavior --- """

def get_stock_price(intent_request):
    symbol = get_slots(intent_request)["symbol"]
     
    sh = StockAPIHandler()
    k = sh.get_stock_price(symbol)
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'Stock Price of {} is ${}'.format(symbol, k)})


""" --- Intents --- """
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers    
    if intent_name == 'StockPrice':
        return get_stock_price(intent_request)        

    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    #os.environ['TZ'] = 'America/New_York'
    #time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)
