import http.client, json, csv, os

#-----------------------------------------------------------
#------------------------ Andy Fiore -----------------------
#-------------------- afiore@juniper.net -------------------
#--- https://github.com/AutomationAndy/Juniper-Mist-API/ ---
#-----------------------------------------------------------

Token = ""

CSVFile = os.path.realpath(os.path.dirname(__file__)) + "\output.csv"

fields = []
rows = []

with open(CSVFile, 'r') as file:
    reader = csv.reader(file)
    fields = next(reader)

    for row in reader:
        if 'id' not in fields:
            print("Expecting column named 'id' in the csv file and couldn't find it. Ending script.")
            break
        if 'site_id' not in fields:
            print("Expecting column named 'site_id' in the csv file and couldn't find it. Ending script.")
            break
        if 'notes' not in fields:
            print("Expecting column named 'notes' in the csv file and couldn't find it. Ending script.")
            break
        
        id = row[fields.index('id')]
        site_id = row[fields.index('site_id')]
        notes = row[fields.index('notes')]

        #print ("Device ID: " + id)
        #print ("Site ID: " + site_id)
        #print ("Notes: " + notes)

        conn = http.client.HTTPSConnection("api.mist.com")
        payload = json.dumps({"notes": "" + notes + ""})
        headers = {
        'Authorization': 'Token {}'.format(Token),
        'Content-Type': 'application/json'
        }
        conn.request("PUT", "/api/v1/sites/{}/devices/{}".format(site_id, id), payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8") + "\n")