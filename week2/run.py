#! /usr/bin/env python3
import os
import requests

directory = "/data/feedback"
feedback_dict = {"title":"","name":"","date":"","feedback":""}

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    #print(file)
    with open(file, 'r') as f:
        for key in feedback_dict.keys():
            #print(key)
            feedback_dict[key] = f.readline().strip()
    response = requests.post("http://34.27.136.45/feedback/", json=feedback_dict)
    print(response.request.url)
    print(response.status_code)
    print(response.request.body)
    #print(feedback_dict)
