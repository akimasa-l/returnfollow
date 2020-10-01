import requests
import requests_oauthlib
import json

url="https://api.twitter.com/1.1/friendships/create.json"
auth={}
with open("./followers.json") as f:
    followers=json.load(f)

for id in followers["ids"]:
    params={"user_id":id,"follow":"true"}
    a=requests.post(url,params=params,auth=auth)
    print(a.status_code)