import httplib, urllib, base64
import json

headers = {
    'api_key': '919aca6de37440c8b9783f96d62f70e8',
}

def query(station):
    url = "/StationPrediction.svc/json/GetPrediction/{0}".format(station)
    print "Querying " + url
    try:
        conn = httplib.HTTPSConnection('api.wmata.com')
        conn.request("GET", url, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print "Oh noes" + str(e)
    print "Got some data! Returning it now."
    return json.loads(data)

response = query("B03")

trains = response['Trains']

for train in trains:
#    print json.dumps(train)
    print train['LocationName']
    print train['DestinationName']
    print train['Min']
	
#if response['Group'] == '1':
#	print "To Glenmont"
#	print train['Min']
#else
#	print "To Shady Grove"
#	print train['Min']
