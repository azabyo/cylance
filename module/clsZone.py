# -*-coding:utf-8-*-

import requests
import json
from clsCylance import Cylance


class zoneAPI(Cylance):
    LOW = "Low"
    MED = "Medium"
    HIGH = "High"

    def createZone(self, _upid, _zname, _criticality=LOW):
        if _pid is None:
            return False

        if _zname is None:
            return False

        payload = {
            "name": _zname,
            "policy_id": _upid,
            "criticality": _criticality
        }

        try:
            resp = requests.post(
                "{}/zones/v2".format(
                    self.API_URL), data=json.dumps(payload),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getZones(self, _page=Cylance.DEFAULT_PAGE,
                 _page_size=Cylance.DEFAULT_PAGE_SIZE):
        try:
            resp = requests.get(
                "{}/zones/v2?page={}&page_size={}".format(
                    self.API_URL, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            # print get_users_resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getDeviceZones(self, _udid, _page=Cylance.DEFAULT_PAGE,
                       _page_size=Cylance.DEFAULT_PAGE_SIZE):
        try:
            resp = requests.get(
                "{}/zones/v2/{}/zones?page={}&page_size={}".format(
                    self.API_URL, _udid, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getZone(self, _uzid):
        if _uzid is None:
            return False

        try:
            resp = requests.get(
                "{}/zones/v2/{}".format(
                    self.API_URL, _uzid),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def updateZone(self, _uzid, _upid, _zname, _criticality=LOW):
        payload = {
            "name": _zname,
            "policy_id": _upid,
            "criticality": _criticality
        }

        try:
            resp = requests.put(
                "{}/zones/v2/{}".format(
                    self.API_URL, _uzid), data=json.dumps(payload),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def deleteZone(self, _uzid):
        try:
            resp = requests.delete(
                "{}/zones/v2/{}".format(
                    self.API_URL, _uzid),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None
