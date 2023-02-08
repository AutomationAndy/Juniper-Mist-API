import http.client, json

#-----------------------------------------------------------
#------------------------ Andy Fiore -----------------------
#-------------------- afiore@juniper.net -------------------
#--- https://github.com/AutomationAndy/Juniper-Mist-API/ ---
#-----------------------------------------------------------


Mist_Org1_Token = ""
Mist_Org1_ID = ""
Mist_Site1_ID = ""
Mist_wlan1_ID = ""

Mist_Org2_Token = ""
Mist_Org2_ID = ""
Mist_Site2_ID = ""


#--------
#Get the WLAN to clone it
conn = http.client.HTTPSConnection("api.mist.com")
payload = ''
headers = {
  'Authorization': 'Token {}'.format(Mist_Org1_Token)
}
conn.request("GET", "/api/v1/sites/{}/wlans/{}".format(Mist_Site1_ID, Mist_wlan1_ID), payload, headers)
res = conn.getresponse()
data = res.read()
jsonData = json.loads(data)

jsonPretty = json.dumps(jsonData, indent=4)
print("Step 1 - Output of WLAN to be cloned")
print(jsonPretty)
#--------

#--------
#Jam the output of the above into the second org/site
conn2 = http.client.HTTPSConnection("api.mist.com")
payload2 = data.decode("utf-8")
headers2 = {
  'Authorization': 'Token {}'.format(Mist_Org2_Token),
  'Content-Type': 'application/json'
}
conn2.request("POST", "/api/v1/sites/321c6ed5-f45a-44ce-a3c4-7cc5d2ac89f8/wlans", payload2, headers2)
res2 = conn2.getresponse()
data2 = res2.read()
jsonData2 = json.loads(data2)

jsonPretty2 = json.dumps(jsonData2, indent=4)
print("Step 2 - Output of attempt to create new WLAN")
print(jsonPretty2)