#!/usr/bin/env python

# Testing ansible inventory via guthub raw files

import argparse
import requests 
import urllib
import os
import re
from time import time
import xmlrpclib

import json
import netifaces
import getmac

gws = netifaces.gateways()
defiface = gws['default'][netifaces.AF_INET][1]

mymac = getmac.get_mac_address(interface=defiface)

url = "https://raw.githubusercontent.com/BruceBushby/provision/master/cmdb/" + mymac
print url
r = requests.get(url)

print r.text

