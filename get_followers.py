import requests
import requests_oauthlib
import json

url="https://api.twitter.com/1.1/followers/ids.json"
auth={}
params={"string_fy_ids":"true","count":"5000"}
a=requests.get(url,auth=auth,params=params)
print(a.status_code)
s=json.dumps(a.text)
with open("./follower.json",mode="w") as f:
    f.write(s)