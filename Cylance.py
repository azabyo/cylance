# -*-coding:utf-8-*-

from module.clsCylance import Cylance, ROOT_PATH
from module.clsDevice import deviceAPI
from module.clsGlobal import globalAPI
from module.clsPolicy import policyAPI
from module.clsUser import userAPI
from module.clsZone import zoneAPI
from module.clsThreat import threatAPI
import json

AZABYO_DID = "938a56e5-d736-431f-9a0a-3f9a3622aeba"
DESKTOP_TBU = "ad2c74d5-a129-4457-9cbb-8643bc9b972d"
TEST_ZONE_ID = "4a7fdbf7-d3c7-4533-a5d5-6ea13a5fb921"
MY_PC_ZONE_ID = "3526b55e-8ca0-4af5-ae29-b3c05c1e756f"
TROUBLESHT_PID = "d7b277fe-2ac3-47f9-bb82-9becf2b4d7b2"
CTMUSD32000_SHA256 = "c5e853eb2b51a5df8ec68a541a9be3cc3785219572ce574929fa92ca9a6e891e"
CTMUSD32000_MD5 = "B3CCBC4AF8977A12E2AEE0C9F7E8E518"
ADD_TEST_SHA256 = "c59b088e106f8dfdc93a35802c8b3c82d6b3f14fca55af9120dfb40b95eb35a1"
YGKANG_UID = "2e442b0d-ce6d-4cdd-9ecc-f5be8a03c009"
TEST_PID = "afb9d559-03d0-4559-877d-e68523b22247"
TEST_PID_LIST = ["39dd1277-9bf7-47c8-8f9c-7a99753418a3",
                 "deb471eb-e1cf-447e-ac02-907b6a84980b"]


def main():
    # ### User API ###
    # print userAPI().getUsers()
    # userAPI().createUser('ygkang_test5@sk.com', _role=userAPI.ZONE_MNGR,
    #                      _zrtype=userAPI.ZONE_MNGR)
    # print userAPI().getUser('ygkang@sk.com')
    # print userAPI().deleteUser('ygkang_test1@sk.com')
    # print userAPI().sendMail('ygkang@sk.com', _invite=False)

    # ### Deviced API ###
    # device = deviceAPI()
    # print deviceAPI().updateDevice("938a56e5-d736-431f-9a0a-3f9a3622aeba",
    #                                "azabyo_update2")
    # print device.getDevices()
    # print device.getDeviceThreats(DESKTOP_TBU)
    # print device.getZoneDevices(MY_PC_ZONE_ID)
    # print device.getAgentInstallerLink()
    # print deviceAPI().getDeviceByMACAddress("08-00-27-27-C2-6A")

    # ### Global API ###
    # print globalAPI().getGlobalList(3)
    # print globalAPI().addToGlobalList(ADD_TEST_SHA256)

    # ### Policy API ###
    print policyAPI().getPolicy("48084450-ea2e-4683-9ed1-36469522f8d9")
    # print policyAPI().getPolicies()
    # print policyAPI().deletePolicy(TEST_PID)
    # print policyAPI().deletePolicies(TEST_PID_LIST)
    # print policyAPI().createPolicy("test_policy", YGKANG_UID)

    # #### Zone API ####
    # print zoneAPI().createZone(_upid=TROUBLESHT_PID, _zname="test_zone")
    # print zoneAPI().getZones()
    # print zoneAPI().getDeviceZones(AZABYO_DID)
    # print zoneAPI().getZone(MY_PC_ZONE_ID)
    # print zoneAPI().updateZone(_upid=TROUBLESHT_PID,
    #                            _uzid="3ee9d754-dd45-4d0a-9a3b-5b915ff0fc33",
    #                            _zname="test_zone_update")
    # print zoneAPI().deleteZone("3ee9d754-dd45-4d0a-9a3b-5b915ff0fc33")

    # ### Threat API ###
    # print threatAPI().getThreat(CTMUSD32000_SHA256)
    # print threatAPI().getThreats()
    # print threatAPI().getThreatDevices(CTMUSD32000_SHA256)
    # print threatAPI().getThreatDownloadURL(CTMUSD32000_SHA256)


if __name__ == "__main__":
    main()
