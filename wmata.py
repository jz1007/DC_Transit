import httplib, urllib, base64, urllib2
import json
import threading, time
import datetime
import os

headers = {
    'api_key': '919aca6de37440c8b9783f96d62f70e8',
}

########TIME TO TRAIN SET-UP#########

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

######END TIME TO TRAIN SET-UP / BEGIN ALERT SET-UP#######

def query(alerts):
	url = "/Incidents.svc/json/Incidents?api_key=919aca6de37440c8b9783f96d62f70e8" ##got lazy on API key
	print "Querying " + url
	try:
		conn = httplib.HTTPSConnection('api.wmata.com')
		conn.request("GET", url)
		response = conn.getresponse()
		data = response.read()
		conn.close()
	except Exception as e:
		print "Oh noz" + str(e)
	print "Returning data now..."
	print ""
	return json.loads(data)

response2 = query("Incidents") 

alerts = response2['Incidents']

#######END ALERT SET-UP########

def minutes():
	os.system("clear")
	times = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S') 
	print ""    
	print "****************"
	print "Trains arriving at Union Station"
	print times
	print "****************"
	print ""
	for train in trains:
		#print json.dumps(train)
		if train['Group'] == '1':
			#print train['LocationName'] + " To Glenmont via Noma"
			#####add in a 'RUN!!!!' print
			print "To Glenmont " + train['Min']				
		
		if train['Group'] == '2':
			#print train['LocationName'] + " To Shady Grove via Metro Center"
			print "To Shady Grove " + train['Min']
		print ""

	print ""
	print "***Alerts***"
	for alert in alerts:
		#print json.dumps(alert)
		print alert['Description']
	threading.Timer(5, minutes).start()
	
minutes()
