# -*-coding:utf-8-*-

import requests
import json
from clsCylance import Cylance


class policyAPI(Cylance):
    CTR_BLOCK = "Block"
    CTR_FULLACCESS = "FullAccess"

    DEV_CLS_ANDROID_USB = "AndroidUSB"
    DEV_CLS_IOS = "iOS"
    DEV_CLS_STILLIMAGE = "StillImage"
    DEV_CLS_USBCDDVDRW = "USBCDDVDRW"
    DEV_CLS_USBDRIVE = "USBDrive"
    DEV_CLS_VMWAREMOUNT = "VMWareMount"
    DEV_CLS_WPD = "WPD"

    DISABLED = "0"
    ENABLED = "1"

    ALERT = "Alert"

    def getPolicy(self, _pid):
        try:
            resp = requests.get(
                "{}/policies/v2/{}".format(
                    self.API_URL, _pid),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def getPolicies(self, _page=Cylance.DEFAULT_PAGE,
                    _page_size=Cylance.DEFAULT_PAGE_SIZE):
        try:
            resp = requests.get(
                "{}/policies/v2?page={}&page_size={}".format(
                    self.API_URL, _page, _page_size),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def createPolicy(self, _policy_name, _uid=None):
        # TODO: 500 error 확인 필요
        if _uid is None:
            return False

        payload = {
            "user_id": _uid,
            "policy": {
                "device_control": {
                    "configurations": [
                        {
                            "control_mode": self.CTR_FULLACCESS,
                            "device_class": self.DEV_CLS_ANDROID_USB
                        },
                        {
                            "control_mode": self.CTR_FULLACCESS,
                            "device_class": self.DEV_CLS_IOS
                        },
                        {
                            "control_mode": self.CTR_FULLACCESS,
                            "device_class": self.DEV_CLS_STILLIMAGE
                        },
                        {
                            "control_mode": self.CTR_FULLACCESS,
                            "device_class": self.DEV_CLS_USBCDDVDRW
                        },
                        {
                            "control_mode": self.CTR_FULLACCESS,
                            "device_class": self.DEV_CLS_USBDRIVE
                        },
                        {
                            "control_mode": self.CTR_FULLACCESS,
                            "device_class": self.DEV_CLS_VMWAREMOUNT
                        },
                        {
                            "control_mode": self.CTR_FULLACCESS,
                            "device_class": self.DEV_CLS_WPD
                        }
                    ],
                    "exclusion_list": []
                },
                "file_exclusions": [],
                "memoryviolation_actions": {
                    "memory_violations": [
                        {
                            "violation_type": "dyldinjection",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "lsassread",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "maliciouspayload",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "outofprocessallocation",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "outofprocessapc",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "outofprocesscreatethread",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "outofprocessmap",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "outofprocessoverwritecode",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "outofprocessunmapmemory",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "outofprocesswrite",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "outofprocesswritepe",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "overwritecode",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "stackpivot",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "stackprotect",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "trackdataread",
                            "action": self.ALERT
                        },
                        {
                            "violation_type": "zeroallocate",
                            "action": self.ALERT
                        }
                    ],
                    "memory_violations_ext": [],
                    "memory_exclusion_list": []

                },
                "policy": [
                    {
                        "name": "auto_blocking",
                        "value": self.ENABLED
                    },
                    {
                        "name": "auto_delete",
                        "value": self.ENABLED
                    },
                    {
                        "name": "auto_uploading",
                        "value": self.ENABLED
                    },
                    {
                        "name": "days_until_deleted",
                        "value": "30"
                    },
                    {
                        "name": "device_control",
                        "value": self.ENABLED
                    },
                    {
                        "name": "full_disc_scan",
                        "value": self.ENABLED
                    },
                    {
                        "name": "kill_running_threats",
                        "value": self.ENABLED
                    },
                    {
                        "name": "logpolicy",
                        "value": self.ENABLED
                    },
                    {
                        "name": "low_confidence_threshold",
                        "value": "-600"
                        # A Cylance Score of -600 to -1000 is Unsafe.
                        # A Cylance Score of 0 to -599 is Abnormal.
                        # A Cyalnce Score greater than 0 is Safe.
                    },
                    {
                        "name": "memory_exploit_detection",
                        "value": self.ENABLED
                    },
                    {
                        "name": "optics",
                        "value": self.ENABLED
                    },
                    {
                        "name": "optics_application_control_auto_upload",
                        "value": self.ENABLED
                    },
                    {
                        "name": "optics_malware_auto_upload",
                        "value": self.ENABLED
                    },
                    {
                        "name": "optics_memory_defense_auto_upload",
                        "value": self.ENABLED
                    },
                    {
                        "name": "optics_script_control_auto_upload",
                        "value": self.ENABLED
                    },
                    {
                        "name": "optics_set_disk_usage_maximum_fixed",
                        "value": "500"
                    },
                    {
                        "name": "prevent_service_shutdown",
                        "value": self.ENABLED
                    },
                    {
                        "name": "sample_copy_path",
                        "value": None
                    },
                    {
                        "name": "scan_exception_list",
                        "value": []
                    },
                    {
                        "name": "scan_max_archive_size",
                        "value": "10"
                    },
                    {
                        "name": "script_control",
                        "value": self.ENABLED
                    },
                    {
                        "name": "show_notifications",
                        "value": self.ENABLED
                    },
                    {
                        "name": "threat_report_limit",
                        "value": "500"
                    },
                    {
                        "name": "trust_files_in_scan_exception_list",
                        "value": self.ENABLED
                    },
                    {
                        "name": "watch_for_new_files",
                        "value": self.ENABLED
                    }
                ]
            },
            "policy_name": _policy_name,
            "script_control": {
                "activescript_settings": {
                    "control_mode": self.ALERT  # Alert, Block
                },
                "global_settings": {
                    "allowed_folders": "",
                    "control_mode": self.ALERT  # 0 - Disabled, 1 - Enabled
                },
                "macro_settings": {
                    "control_mode": self.ALERT  # Alert, Block
                },
                "powershell_settings": {
                    "console_mode": self.ALERT,
                    "control_mode": self.ALERT  # Alert, Block
                }
            },
            "filetype_actions": {
                "suspicious_files": [
                    {
                        "actions": self.ENABLED,  # 0 - Disabled, 1 - Enabled
                        "file_type": "executable"
                    }
                ],
                "threat_files": [
                    {
                        "actions": self.ENABLED,
                        "file_type": "executable"
                    }
                ]
            },
            "logpolicy": {
                "log_upload": self.ENABLED,  # 0 - Disabled, 1 - Enabled
                "maxlogsize": "24",
                "retentiondays": "1"
            }
        }

        try:
            resp = requests.post(
                "{}/policies/v2".format(
                    self.API_URL), data=json.dumps(payload),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def updatePolicy(self):
        # TODO: create policy와 대동소이
        pass

    def deletePolicy(self, _tpid):
        try:
            resp = requests.delete(
                "{}/policies/v2/{}".format(
                    self.API_URL, _tpid),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None

    def deletePolicies(self, _tpid_list=[]):
        if len(_tpid_list) == 0:
            return False

        payload = {
            "tenant_policy_ids": _tpid_list
        }

        try:
            resp = requests.delete(
                "{}/policies/v2".format(
                    self.API_URL), data=json.dumps(payload),
                headers=self.getHeader(), verify=self.verify)
            print resp.status_code
            return resp.text
        except Exception as ex:
            print ex
            return None
