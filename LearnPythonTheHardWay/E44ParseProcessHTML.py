# July 2020
# PARSE AND PROCESS HTML

# RETRIEVE DATA FROM THE INTERNET
import urllib.request

# 1. Connect
webUrl=urllib.request.urlopen('http://www.google.com')
print('Result code: ' + str(webUrl.getcode())) # This checks the success of the connection
# 2. Read Data
data=webUrl.read()
print(data)

# GET DATA FROM A SOURCE: Json
import json
# define a variable to hold the source URL
# In this case we'll use the free data feed from the USGS
# This feed lists all earthquakes for the last day larger than Mag 2.5
urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
# Open the URL and read the data
webUrl = urllib.request.urlopen(urlData)
print ("result code: " + str(webUrl.getcode()))
# Let's define a function to print
def printResult(data):
    #Use json module to load the string data into a dictionary
    theJSONn=json.loads(data)
    print(type(theJSONn))

    # In each json file there are sections to describe the file. It is documented in the manual
    # now we can access the contents of the JSON like any other Python object
    if 'title' in theJSONn['metadata']: # Calling like dictionary
        print(theJSONn['metadata']['title'])

    # output the number of events, plus the magnitude and each event name
    count=theJSONn['metadata']['count']
    print(str(count)+ 'events recorded')

    # for each event, print the place where it occurred
    for i in theJSONn['features']:
        print (i['properties']['place'])
    print('............\n')

    # print the events that only have a magnitude greater than 4
    for i in theJSONn['features']:
        if (i['properties']['mag'])>=0:
            print("%2.1f" %i['properties']['mag'],i['properties']['place'])
    print('............\n')

    # print only the events where at least 1 person reported feeling something
    print('Events that were felt:')
    for i in theJSONn['features']:
        feltReport=i['properties']['felt']
        if feltReport!=None:
            if feltReport>0:
                print("%2.1f" % i['properties']['mag'], i['properties']['place'],'Reported' + str(feltReport) + 'times')

# Used to print the data if the code is correct
if (webUrl.getcode()==200):
    data=webUrl.read()
    printResult(data)
else:
    print('Error')