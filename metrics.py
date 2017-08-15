"""
Created on 2015-12-16
@author: Asma Shajrawi - Esprida

This code sends metric data in a JSON with an HTTP POST to the LiveIntersect server (hardcoded)

Refer to Developer Guide> Endpoint API Entities> Asset Registration > Asset Metrics under the Help Section on your of you LiveIntersect's 
Admisniatrtion dashboard 

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
                    "detectionTime":"2017-01-20T18:46:32Z"
            },
            {
                    "metricValue": "24",
                    "detectionTime":"2017-01-20T18:46:32Z"
            }
        ]
    },
    {
        "metricCode":"Humidity",
        "values":[
            {
                    "metricValue": "30",
                    "detectionTime":"2017-01-20T18:46:32Z"
            }
        ]
    }
]
# POST with JSON 

url = 'http://sandbox.liveintersect.com.com/agentapi/assetmetrics'
headers = {'content-type': 'application/json', 'Authorization': "Basic MzRiNjNkYmMtZWIzZS00MTAxLTgzM2QtYmE4MjAzNWRjOGEzOg=="} #This is general/default
req = urllib2.Request(url,data = json.dumps(AssetMetric_Data), headers = headers)
response = urllib2.urlopen(req)
print response.read()
if response.status_code == "200":
    print("metrics successfully delivered.")
else:
    print("Error sending metrics")
    print response.status_code
    print response.text
    
response.close()

   
 
