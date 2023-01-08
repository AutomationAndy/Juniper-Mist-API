import http.client, json

#-----------------------------------------------------------
#------------------------ Andy Fiore -----------------------
#-------------------- afiore@juniper.net -------------------
#--- https://github.com/AutomationAndy/Juniper-Mist-API/ ---
#-----------------------------------------------------------


Token = ""
TokenID = ""

conn = http.client.HTTPSConnection("api.mist.com")
payload = ''
headers = {
  'Authorization': 'Token {}'.format(Token)
}
conn.request("DELETE", "/api/v1/self/apitokens/{}".format(TokenID), payload, headers)
res = conn.getresponse()
data = res.read()
jsonData = json.loads(data)

jsonPretty = json.dumps(jsonData, indent=4)
print(jsonPretty)