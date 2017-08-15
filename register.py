"""
Created on 2015-12-16
@author: AShajrawi

This is an agent code that registers the agent/remote device/thing as an root asset on the LiveIntersect server.
It sends the registration data in a JSON with an HTTP POST to the server (hardcoded).

Refer to the documentation under Developer Guide> Endpoint API Entities> Asset Registration Under the Help section of your 
LiveIntersect Administration Dashboard.

Agent:Register
-->Register method is used to create an assets.  A JSON object is passed to the server as part 
of the request.
"""

import urllib2, json


"""Defing the dictionary with the device registration data. 
This dictionary will be converted to JSON in the HTTP POST"""

Registeration_Data = 
{
	'apiKey': "0559fcd2-6a08-4882-930c-447ee505c89b", #the API KEY can be generated using the developer tools LiveIntersect Administration Dashboard. It is unique to each org and should be hardcoded on the agent for autherization
	'srNo': "ffff017692g579",
	'assetName': "DigiModem-TransPort-WR21",
	'assetTypeCode': "Cellular-modem",
    'timeZoneId': "Etc/GMT-8"
}

# POST with JSON 

url = 'http://sandbox.liveintersect.com/agentapi/registration'
headers = {'content-type': 'application/json'} #This is general/default
req = urllib2.Request(url,data = json.dumps(Registeration_Data), headers = headers)
response = urllib2.urlopen(req)
print response.read()
response.close()
 
