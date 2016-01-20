"""
Created on 2015-12-16
@author: AShajrawi

This is an agent code that registers the agent/remote device/thing as a root asset on the LiveControl server.
It sends the registration data in a JSONan with an HTTP POST to the server (hardcoded).

Refer to http://docs.esprida.com/pages/viewpage.action?title=API+Reference&spaceKey=PR#APIReference-

Agent:Register
-->Register method is used to create root assets.  A JSON object is passed to the server as part 
of the request.
"""

import urllib2, json


"""Defing the dictionary with the device registration data. 
This dictionary will be converted to JSON in the HTTP POST"""

Registeration_Data = {
    'apiKey':"c5739b77-e349-4953-8c7d-fb158ab2895f", #the API KEY is unique to each asset and should be hardcoded on the agent
    'srNo':"469698",
    'assetName':"Digi modem - TransPort WR21",
    'assetTypeCode':"Cellular-modem",
    "timeZoneId" : "America/Toronto"
}

# POST with JSON 

url = 'http://demo8.esprida.com/agentapi/register'
headers = {'content-type': 'application/json'} #This is general/default
req = urllib2.Request(url,data = json.dumps(Registeration_Data), headers = headers)
response = urllib2.urlopen(req)
print response.read()
response.close()
 
