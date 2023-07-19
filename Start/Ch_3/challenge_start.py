# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD


def getsig(item):
    sig = item["properties"]["sig"]
    if sig is None:
        return 0
    return sig


significant_events = sorted(data["features"], key=getsig, reverse=True)
significant_events = significant_events[:40]
significant_events.sort(key=lambda q: q["properties"]["time"], reverse=True)

rows = []
headers = ["Magnitude", "Place", "Felt Reports", "Date", "Link"]

for event in significant_events:
    dt = datetime.date.fromtimestamp(int(event["properties"]["time"]) / 1000)
    lat = event["geometry"]["coordinates"][1]
    long = event["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{long}"
