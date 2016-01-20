"""
Created on 2015-12-16
@author: AShajrawi

This code simulates the AssetMetric part of the Agent API. it sends "POST" to the bachchan server 
hardcoded data in a JSON to test the connectiom and the JASON contents.

Refer to http://docs.esprida.com/pages/viewpage.action?title=API+Reference&spaceKey=PR#APIReference-Agent:AssetMetric

This code create or update metrics associated with an asset.  
A JSON object is passed to the server as part of the request.
"""

import urllib2, json

"""Defing the dictionary with the device registration data. 
This dictionary will be converted to JSON in the POST"""
AssetMetric_Data = [
    {
        "metricCode":"Soil.Temperature",
        "values":[
            {
                    "metricValue": "21",
                    "detectionTime":"2016-01-20T18:46:32Z"
            },
            {
                    "metricValue": "24",
                    "detectionTime":"2016-01-20T18:46:32Z"
            }
        ]
    },
    {
        "metricCode":"Humidity",
        "values":[
            {
                    "metricValue": "30",
                    "detectionTime":"2016-01-20T18:46:32Z"
            }
        ]
    }
]
# POST with JSON 

url = 'http://demo8.esprida.com/agentapi/assetmetrics'
headers = {'content-type': 'application/json', 'Authorization': "Basic MzRiNjNkYmMtZWIzZS00MTAxLTgzM2QtYmE4MjAzNWRjOGEzOg=="} #This is general/default
req = urllib2.Request(url,data = json.dumps(AssetMetric_Data), headers = headers)
response = urllib2.urlopen(req)
print response.read()
response.close()

   
 
