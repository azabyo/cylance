# -*-coding:utf-8-*-

import requests
import json
from clsCylance import Cylance


class userAPI(Cylance):
    NONE = "None"
    USER = "User"
    ADMIN = "Administrator"
    ZONE_MNGR = "Zone Manager"
    MAX_NAME_COUNT = 64
    ROLE0 = "00000000-0000-0000-0000-000000000000"
    ROLE1 = "00000000-0000-0000-0000-000000000001"
    ROLE2 = "00000000-0000-0000-0000-000000000002"
    ROLE3 = "00000000-0000-0000-0000-000000000003"
    DEFAULT_ZONE = "null"

    ALREADY_ID_MSG = "Already User ID."

    def getRole(self, _role=None):
        role_dict = {
            self.USER: self.ROLE1,
            self.ADMIN: self.ROLE2,
            self.ZONE_MNGR: self.ROLE3
        }
        if _role is not None:
            if _role in role_dict:
                return role_dict[_role]
        return None

    def getZoneRole(self, _role=None):
        zone_role_dict = {
            self.NONE: self.ROLE0,
            self.ZONE_MNGR: self.ROLE1,
            self.USER: self.ROLE2
        }
        if _role is not None:
            if _role in zone_role_dict:
                return zone_role_dict[_role]
        return None

    def getUsers(self, _page=Cylance.DEFAULT_PAGE,
                 _page_size=Cylance.DEFAULT_PAGE_SIZE):
        try:
            get_users_resp = requests.get(
                "{}/users/v2?page={}&page_size={}".format(
                    self.API_URL, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            # print get_users_resp.status_code
            return get_users_resp.text
        except Exception as ex:
            print ex
            return None

    def createUser(self, _email, _f_name="", _l_name="", _role=USER,
                   _zid=DEFAULT_ZONE, _zrtype=USER, _zrname="", _is_zone=False):

        if len(_f_name) > self.MAX_NAME_COUNT:
            return None
        if len(_l_name) > self.MAX_NAME_COUNT:
            return None

        user_info = self.getUser(_email)
        if user_info != "":
            return self.ALREADY_ID_MSG

        payload = {
            "email": _email,
            "user_role": self.getRole(_role),
            "first_name": _f_name,
            "last_name": _l_name,
            "zones": []
        }

        if _role != self.ADMIN:
            zones = []
            zone_info = json.loads(zoneAPI().getZones())
            for i in zone_info["page_items"]:
                if _zrname == "":
                    zones.append(
                        {"id": i["id"], "role_type": self.getZoneRole(_zrtype)})
                else:
                    # if _zrname == i[""]
                    zones.append(
                        {"id": i["id"], "role_type": self.getZoneRole(_zrtype)})
            payload.update({"zones": zones})

        try:
            resp = requests.post(
                "{}/users/v2".format(self.API_URL),
                headers=self.getHeader(_scp="user:create", _force=True),
                data=json.dumps(payload), verify=self.verify)
            print resp.status_code
            print resp.text
        except Exception as ex:
            print ex

    def getUser(self, _user_email):
        try:
            resp = requests.get(
                "{}/users/v2/{}".format(
                    self.API_URL, _user_email),
                headers=self.getHeader(), verify=self.verify)
            # print get_users_resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def updateUser(self, _user_id):
        pass

    def deleteUser(self, _user_email):
        if _user_email.find("@") > 0:
            user_info = self.getUser(_user_email)
            if user_info is not None:
                user_id = json.loads(user_info)["id"]
            else:
                return False
        else:
            return False

        try:
            resp = requests.delete(
                "{}/users/v2/{}".format(
                    self.API_URL, user_id),
                headers=self.getHeader(), verify=self.verify)
            return True
        except Exception as ex:
            print ex
            return False

    def sendInviteEmail(self, _user_email):
        try:
            resp = requests.post(
                "{}/users/v2/{}/invite".format(self.API_URL, _user_email),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex

    def sendResetPasswordEmail(self, _user_email):
        try:
            resp = requests.post(
                "{}/users/v2/{}/resetpassword".format(
                    self.API_URL, _user_email),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex

    def sendMail(self, _user_email, _invite=True):
        if _invite:
            uri = "invite"
        else:
            uri = "resetpassword"
        try:
            resp = requests.post(
                "{}/users/v2/{}/{}".format(
                    self.API_URL, _user_email, uri),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
