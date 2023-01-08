import http.client, json

#-----------------------------------------------------------
#------------------------ Andy Fiore -----------------------
#-------------------- afiore@juniper.net -------------------
#--- https://github.com/AutomationAndy/Juniper-Mist-API/ ---
#-----------------------------------------------------------


Token = ""

conn = http.client.HTTPSConnection("api.mist.com")
payload = ''
headers = {
  'Authorization': 'Token {}'.format(Token)
}
conn.request("GET", "/api/v1/self/apitokens", payload, headers)
res = conn.getresponse()
data = res.read()
jsonData = json.loads(data)

jsonPretty = json.dumps(jsonData, indent=4)
print(jsonPretty)