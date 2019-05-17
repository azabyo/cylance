# -*-coding:utf-8-*-

import requests
import json
from clsCylance import Cylance


class globalAPI(Cylance):
    GlobalQuarantine = 0
    GlobalSafe = 1
    GlobalQuarantine_STR = "GlobalQuarantine"
    GlobalSafe_STR = "GlobalSafe"

    CAT_ADMIN = "Admin Tool"
    CAT_COMMERCIAL = "Commercial Software"
    CAT_DRIVERS = "Drivers"
    CAT_INT_APP = "Internal Application"
    CAT_OS = "Operating System"
    CAT_NONE = "None"

    def getGlobalList(self, _list_type=GlobalQuarantine,
                      _page=Cylance.DEFAULT_PAGE,
                      _page_size=Cylance.DEFAULT_PAGE_SIZE):

        if _list_type != self.GlobalQuarantine and _list_type != self.GlobalSafe:
            return False

        try:
            resp = requests.get(
                "{}/globallists/v2?listTypeId={}&page={}&page_size={}".format(
                    self.API_URL, _list_type, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def addToGlobalList(self, _sha256, _list_type=GlobalQuarantine_STR,
                        _category=CAT_NONE, _reason="N/A"):
        payload = {"sha256": _sha256, "list_type": _list_type,
                   "category": _category, "reason": _reason}

        try:
            resp = requests.post("{}/globallists/v2".format(self.API_URL),
                                 data=json.dumps(payload),
                                 headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def deleteFromGlobalList(self, _sha256, _list_type=GlobalQuarantine_STR):
        payload = {"sha256": _sha256, "list_type": _list_type}

        try:
            resp = requests.delete("{}/globallists/v2".format(self.API_URL),
                                   data=json.dumps(payload),
                                   headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None
