#!-*-coding:utf-8-*-

import jwt  # PyJWT version 1.5.3 as of the time of authoring.
import uuid
import requests  # requests version 2.18.4 as of the time of authoring.
import json
import os
from datetime import datetime, timedelta


ROOT_PATH = os.path.dirname(os.path.join("..", os.path.dirname(__file__)))


class Cylance(object):
    TIMEOUT = 1800
    # The tenant's unique identifier.
    TID = "f7357359-b236-4277-8fe4-f01dfd73a5de"
    # The application's unique identifier.
    APP_ID = "0554d84b-c567-48d4-a720-cee2dad7631f"
    # The application's secret to sign the auth token with.
    APP_SECRET = "f6fa0a98-d662-4c14-8149-85d9b47e72b7"

    API_URL = "https://protectapi{}.cylance.com".format("-au")
    AUTH_URL = "{}/auth/v2/token".format(API_URL)
    ISS_URL = "http://cylance.com"

    DEFAULT_PAGE = 1
    DEFAULT_PAGE_SIZE = 200

    def __init__(self, _access_token=None):
        self.verify = False
        self.access_token = _access_token
        self.last_access_token = None

    def mkJWT(self, _scp=None):
        self.now = datetime.utcnow()
        self.timeout_datetime = self.now + timedelta(seconds=self.TIMEOUT)
        epoch_time = int((self.now - datetime(1970, 1, 1)).total_seconds())
        epoch_timeout = int(
            (self.timeout_datetime - datetime(1970, 1, 1)).total_seconds())
        claims = {"exp": epoch_timeout,
                  "iat": epoch_time,
                  "iss": self.ISS_URL,
                  "sub": self.APP_ID,
                  "tid": self.TID,
                  "jti": str(uuid.uuid4())
                  #   "scp": "user:list"
                  }
        if _scp is not None:
            claims["scp"] = _scp
            print claims
        encoded = jwt.encode(claims, self.APP_SECRET, algorithm='HS256')
        return encoded

    def getAccessToken(self, _scp=None):
        payload = {"auth_token": self.mkJWT(_scp)}
        headers = {"Content-Type": "application/json; charset=utf-8",
                   "Accept": "application/json"}
        try:
            resp = requests.post(self.AUTH_URL, headers=headers,
                                 data=json.dumps(payload), verify=self.verify)
        except Exception as ex:
            print ex
            return None

        if len(resp.text) > 0:
            return json.loads(resp.text)['access_token']
        else:
            return None

    def writeAccessToken(self):
        try:
            with open(
                    os.path.join(ROOT_PATH, "current_access_token.txt"), "w") as f:
                f.write(self.access_token)
            return True
        except Exception as ex:
            print ex
            return False

    def getHeader(self, _scp=None, _force=False):
        if _force:
            self.last_access_token = self.access_token
            self.access_token = self.getAccessToken(_scp)
        else:
            if self.access_token is None:
                self.access_token = self.getAccessToken(_scp)
                self.last_access_token = self.access_token

            elif self.timeout_datetime < datetime.utcnow():
                self.last_access_token = self.access_token
                self.access_token = self.getAccessToken(_scp)

        return_hearers = {"Authorization": "Bearer "+self.access_token,
                          "Accept": "application/json",
                          "Content-Type": "application/json; charset=utf-8"}

        return return_hearers
