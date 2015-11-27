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
        print "Oh noz" + str(e)
    print "Returning data now..."
    print ""
    return json.loads(data)

response = query("B03")

trains = response['Trains']

#########sorting??? sort by groups here

for train in trains:
	#print json.dumps(train)
	if train['Group'] == '1':
		#print train['LocationName'] + " To Glenmont via Noma"
		print "To Glenmont " + train['Min']
		
	if train['Group'] == '2':
		#print train['LocationName'] + " To Shady Grove via Metro Center"
		print "To Shady Grove " + train['Min']
	print ""
