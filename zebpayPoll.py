import urllib, json, datetime, pymongo, pprint
from pymongo import MongoClient

url = "https://www.zebapi.com/api/v1/market/ticker/btc/inr"
try:
    result = json.load(urllib.urlopen(url))
    result['timestamp'] = datetime.datetime.now()
except:
    print "URL Not Reachable"

try:
    client = MongoClient('mongodb://heroku_2r0ssk14:ca0rje96ensho8arjrv65k69ls@ds161164.mlab.com:61164/heroku_2r0ssk14')
    db = client.heroku_2r0ssk14
    zebpay_data = db.zebpay_datapoints
    datapoint_id = zebpay_data.insert_one(result).inserted_id
    pprint.pprint(zebpay_data.find_one({"_id": datapoint_id}))
except:
    print "DB Not reachable"



