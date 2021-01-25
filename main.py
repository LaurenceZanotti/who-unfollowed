import json

followers = None
following = None

with open('followers.json') as file:
    followers = file.read()

with open('following.json') as file:
    following = file.read()

print(json.loads(following))


