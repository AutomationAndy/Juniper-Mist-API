import http.client, json, csv, os

#-----------------------------------------------------------
#------------------------ Andy Fiore -----------------------
#-------------------- afiore@juniper.net -------------------
#--- https://github.com/AutomationAndy/Juniper-Mist-API/ ---
#-----------------------------------------------------------

Token = ""
OrgID = ""

conn = http.client.HTTPSConnection("api.mist.com")
payload = ''
headers = {
  'Authorization': 'Token {}'.format(Token)
}
conn.request("GET", "/api/v1/orgs/{}/inventory".format(OrgID), payload, headers)
res = conn.getresponse()
data = res.read()
jsonData = json.loads(data)

jsonPretty = json.dumps(jsonData, indent=4)
print(jsonPretty)

#This is where we build the headers for each column dynamically, so that if the API call changes in the future, this code will still work just fine.
CSVfields = []
CSVrow = []
for x in jsonData:
            keys = x.keys()
            #This section of the for loop steps through all of the keys in jsonData. If you un-comment the next line, you can see the output, but you'll also see it spits out every single block and depending on what you have in your inventory, the keys are different, so we need to account for that.
            #print(keys)
            for x in keys:
                #This section breaks up the keys above, so we can futher manipulate the data. If you uncomment the next line you'll see it'll spit out all the keys for each block, but there are tons of duplicates. We only want one column for each key.
                #print(x)
                if x not in CSVfields:
                    CSVfields.append(x)

#Uncomment the next line to see what lines 26 through 35 have built. Now we have each key in the list, and theres only one entry for it. Now we can feed this to the CSV writer to write the first row of the CSV with this info
#print(CSVfields)

CSVFile = os.path.realpath(os.path.dirname(__file__)) + "\output.csv"

with open(CSVFile, 'w', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    writer = csv.writer(csvfile)
    fields = CSVfields
    writer.writerow(fields)

    i = 0
    for x in jsonData:
            for y in CSVfields:
                if y in jsonData[i]:
                    CSVrow.append(jsonData[i][y])
            writer.writerow(CSVrow)
            CSVrow = []
            i += 1