# -*-coding:utf-8-*-

import requests
import json
from clsCylance import Cylance


class deviceAPI(Cylance):
    def getDevices(self, _page=Cylance.DEFAULT_PAGE,
                   _page_size=Cylance.DEFAULT_PAGE_SIZE):
        try:
            resp = requests.get(
                "{}/devices/v2?page={}&page_size={}".format(
                    self.API_URL, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            # print get_users_resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getDevice(self, _udid):
        try:
            resp = requests.get(
                "{}/devices/v2/{}".format(
                    self.API_URL, _udid),
                headers=self.getHeader(), verify=self.verify)
            # print get_users_resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def updateDevice(self, _udid, _name=None, _pid=None):
        payload = {}
        if _name is not None:
            payload.update({"name": _name})
        payload.update({"policy_id": ""})

        try:
            resp = requests.put(
                "{}/devices/v2/{}".format(
                    self.API_URL, _udid),
                headers=self.getHeader(), data=json.dumps(payload),
                verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getDeviceThreats(self, _udid, _page=Cylance.DEFAULT_PAGE,
                         _page_size=Cylance.DEFAULT_PAGE_SIZE):
        try:
            resp = requests.get(
                "{}/devices/v2/{}/threats?page={}&page_size={}".format(
                    self.API_URL, _udid, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getZoneDevices(self, _uzid, _page=Cylance.DEFAULT_PAGE,
                       _page_size=Cylance.DEFAULT_PAGE_SIZE):
        try:
            resp = requests.get(
                "{}/devices/v2/{}/devices?page={}&page_size={}".format(
                    self.API_URL, _uzid, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getAgentInstallerLink(self, _product="Protect", _os="Windows",
                              _arch="X64", _pkg="Exe", _build=None):
        product_list = ["protect", "optics"]
        os_list = ["centos7", "linux", "mac",
                   "ubuntu1404", "ubuntu1604", "windows"]
        arch_list = ["x86", "x64", "centos6", "centos6ui", "centos7",
                     "centos7ui", "ubuntu1404", "ubuntu1404ui", "ubuntu1604",
                     "ubunt1604ui"]
        pkg_list = ["exe", "msi", "dmg", "pkg"]

        if _product.lower() not in product_list:
            return False
        if _os.lower() not in os_list:
            return False
        if _arch.lower() not in arch_list:
            return False
        if _pkg.lower() not in pkg_list:
            return False

        req_url = "{}/devices/v2/installer?product={}".format(
            self.API_URL, _product)
        req_url += "o&s={}&package={}&architecture={}".format(_os, _pkg, _arch)

        if _build is not None:
            req_url += "&build={}".format(_build)

        try:
            resp = requests.get(
                req_url, headers=self.getHeader(), verify=self.verify)
            return resp.text
        except Exception as ex:
            print ex
            return None

    def deleteDevices(self):
        pass

    def getDeviceByMACAddress(self, _mac):
        if len(_mac) != 17:
            return False

        try:
            resp = requests.get("{}/devices/v2/macaddress/{}".format(
                self.API_URL, _mac), headers=self.getHeader(),
                verify=self.verify)
            return resp.text
        except Exception as ex:
            print ex
            return None
