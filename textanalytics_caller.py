import requests
# pprint is used to format the JSON response
from pprint import pprint
import json
import os

subscription_key = "subscriptionkey"
endpoint = "myendpoint"

sentiment_url = endpoint + "/text/analytics/v2.1/sentiment"

with open('second_level_comments.json') as json_file:
    data3 = json.load(json_file)
    #print(type(json.loads(data1)))
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_url, headers=headers, json=json.loads(data3))
    sentiments = response.json()
    with open('second_level_comments_response.json', 'w') as f:
        json.dump(sentiments, f)


with open('first_level_comments.json') as json_file:
    data1 = json.load(json_file)
    #print(type(json.loads(data1)))
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_url, headers=headers, json=json.loads(data1))
    sentiments = response.json()
    with open('first_level_comments_response.json', 'w') as f:
        json.dump(sentiments, f)

with open('submissions.json') as json_file:
    data2 = json.load(json_file)

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_url, headers=headers, json=json.loads(data2))
    sentiments = response.json()
    with open('submissions_response.json', 'w') as f:
        json.dump(sentiments, f)
