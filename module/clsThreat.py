# -*-coding:utf-8-*-

import requests
import json
from clsCylance import Cylance


class threatAPI(Cylance):
    def getThreat(self, _hash):
        try:
            resp = requests.get(
                "{}/threats/v2/{}".format(
                    self.API_URL, _hash),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getThreats(self, _page=Cylance.DEFAULT_PAGE,
                   _page_size=Cylance.DEFAULT_PAGE_SIZE):
        try:
            resp = requests.get(
                "{}/threats/v2?page={}&page_size={}".format(
                    self.API_URL, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            # print get_users_resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getThreatDevices(self, _hash, _page=Cylance.DEFAULT_PAGE,
                         _page_size=Cylance.DEFAULT_PAGE_SIZE):
        try:
            resp = requests.get(
                "{}/threats/v2/{}/devices?page={}&page_size={}".format(
                    self.API_URL, _hash, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getThreatDownloadURL(self, _hash):
        # TODO : getThreat()랑 같은 URL로 확인필요함
        try:
            resp = requests.get(
                "{}/threats/v2/{}".format(
                    self.API_URL, _hash),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None
