import jwt  # PyJWT version 1.5.3 as of the time of authoring.
import uuid
import requests  # requests version 2.18.4 as of the time of authoring.
import json
from datetime import datetime, timedelta

# 30 minutes from now
timeout = 1800
now = datetime.utcnow()
# now = datetime.now()
print now
# exit()
timeout_datetime = now + timedelta(seconds=timeout)
epoch_time = int((now - datetime(1970, 1, 1)).total_seconds())
epoch_timeout = int((timeout_datetime - datetime(1970, 1, 1)).total_seconds())

jti_val = str(uuid.uuid4())
# The tenant's unique identifier.
tid_val = "f7357359-b236-4277-8fe4-f01dfd73a5de"
# The application's unique identifier.
app_id = "0554d84b-c567-48d4-a720-cee2dad7631f"
# The application's secret to sign the auth token with.
app_secret = "f6fa0a98-d662-4c14-8149-85d9b47e72b7"

AUTH_URL = "https://protectapi-au.cylance.com/auth/v2/token"
claims = {"exp": epoch_timeout,
          "iat": epoch_time,
          "iss": "http://cylance.com",
          "sub": app_id,
          "tid": tid_val,
          "jti": jti_val
          # The following is optional and is being noted here as an example on how one can restrict
          # the list of scopes being requested
          # "scp": "policy:create, policy:list, policy:read, policy:update"
          }
encoded = jwt.encode(claims, app_secret, algorithm='HS256')
print "auth_token:\n" + encoded + "\n"
payload = {"auth_token": encoded}
headers = {"Content-Type": "application/json; charset=utf-8"}
resp = requests.post(AUTH_URL, headers=headers,
                     data=json.dumps(payload), verify=False)
print "http_status_code: " + str(resp.status_code)
# print "access_token:\n" + json.loads(resp.text)['access_token'] + "\n"
# print resp.text

access_token = json.loads(resp.text)['access_token']

users_headers = {"Authorization": "Bearer "+access_token, "Accept": "application/json",
                 "Content-Type": "application/json; charset=utf-8"}

# users_headers = {}
print users_headers

get_users_resp = requests.get(
    "https://protectapi-au.cylance.com/devices/v2",
    headers=users_headers, verify=False)
# print get_users_resp.status_code
print get_users_resp.text
