import http.client, json

#-----------------------------------------------------------
#------------------------ Andy Fiore -----------------------
#-------------------- afiore@juniper.net -------------------
#--- https://github.com/AutomationAndy/Juniper-Mist-API/ ---
#-----------------------------------------------------------

#Put your API token here, otherwise you'll get a "detail": "Invalid token header. No credentials provided." error.
Token = ""
#Put the ID of the token you want to delete here:
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