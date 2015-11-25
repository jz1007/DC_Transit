import httplib, urllib, base64

headers = {
    # Request headers
    'api_key': '919aca6de37440c8b9783f96d62f70e8',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/StationPrediction.svc/json/GetPrediction/B03", "{body}", headers)
    conn.request("GET", "/StationPrediction.svc/json/GetPrediction/B04", "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
