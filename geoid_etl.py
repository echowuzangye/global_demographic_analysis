import json
import requests
import csv


API_key = '7c6446e2575bb0cc561bd309a671c07bb31adb10'
idb_url = 'https://api.census.gov/data/timeseries/idb/1year?'

# get country name and its GEO_ID

# Show female population aged 15-49 by single year of age for China, India, and Nigeria from 2023-2033: 
# api.census.gov/data/timeseries/idb/1year?get=NAME,GENC,POP&YR=2023:2033&AGE=15:49&SEX=2&for=genc+standard+countries+and+areas:CN,IN,NG&key=YOUR_KEY_GOES_HERE


response = requests.get(idb_url + 'get=NAME,GEO_ID,POP&YR=2023&AGE=15&SEX=2&key=' + API_key)
data = response.json()


with open(f'geoid.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        # Write each data row to the CSV file
        for row in data:
            writer.writerow(row)

