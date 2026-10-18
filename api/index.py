import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for ques in response.json()['items']:
    if ques['answer_count'] == 0:
        print(ques['title'])
        print(ques['link'])
    else:
        print("Skipped")
    print()