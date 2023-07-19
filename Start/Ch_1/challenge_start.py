# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1
print(data["metadata"]["count"])


# 2
def feltreport(q):
    f = q["properties"]["felt"]
    return f is not None and f >= 100


result = list(filter(feltreport, data["features"]))
print(len(result))


# 3
def getfelt(q):
    f = q["properties"]["felt"]
    if f is None:
        return 0
    return f


mostfeltquake = max(data["features"], key=getfelt)
print(
    f"Most felt reports: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}"
)

# 4


def getsig(q):
    f = q["properties"]["sig"]
    if f is None:
        return 0
    return f


sigevents = sorted(data["features"], key=getsig, reverse=True)

for i in range(10):
    print(
        f"Event: {sigevents[i]['properties']['title']}, Significance: {sigevents[i]['properties']['sig']}"
    )
