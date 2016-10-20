#!/usr/bin/python
# created by sfzhang 2016.10.13
import argparse
import json
import sys

inventory_dict = {
                    "webserver" : {
                         "hosts" : [
                                  "ww1.sfzhang.com",
                                  "ww2.sfzhang.com",
                                  "ww3.sfzhang.com"
                                  ],
                         "vars" : {
                            "dns" : "dns.sfzhang.com",
                            "ntp" : "ntp.sfzhang.com",
                            "ipa" : "ipa.sfzhang.com"
                                  }
                                  },
                      
                    "dbserver" : {
                         "hosts" : [
                                  "192.168.65.111",
                                  "192.168.65.222",
                                  "192.168.65.333"
                                  ],
                         "vars" : {
                            "platform" : "RHEL7.0"
                                  }
                                  }
                  }
  
if __name__ == "__main__":
    parser =  argparse.ArgumentParser(prog="dynamic_inventory", description="create ansible dynamic inventory file")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--host", action="store_false")
    if parser.parse_args().list:
        print(json.dumps(inventory_dict))
    else:
        print(json.dumps({}))
