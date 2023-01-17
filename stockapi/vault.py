import base64
import hvac
import json

#local
#fh = open('./test_container_required.json',)

fh = open('/creds/container_required.json',)
my_dict = json.load(fh)
username = my_dict['postgres_user']
password = my_dict['psotgres_pass']
dbhost = my_dict['postgres_dbhost']
database = my_dict['postgres_dbname']
GOOGLE_CLIENT_ID = my_dict['psotgres_pass']
GOOGLE_CLIENT_SECRET = my_dict['psotgres_pass']


