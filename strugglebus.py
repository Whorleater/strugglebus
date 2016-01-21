#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os.path
from datetime import date
from distutils import util

def getFile():
    if ((os.path.isfile("strugglebus.json")) == False):
        file = open('strugglebus.json', 'w+')
        strugglebus = {}
        file.write(json.dumps(strugglebus, sort_keys=True, indent=4, separators=(',', ': ')))
        file.close()

    
def writeStruggle(inputDate, struggle, reasons, solved):
    with open("strugglebus.json", "r+") as data_file:
        
        data = json.load(data_file)
        struggleInfo = {}
        struggleInfo["biggestStruggle"] = struggle
        struggleInfo["why"] = reasons
        struggleInfo["solved"] = solved
        data[inputDate] = struggleInfo
        data_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    
def main():
    inputDate = date.today().isoformat()
    struggle = raw_input("What was today's biggest struggle?")
    reasons = raw_input("Why did you have that struggle?")
    solved = util.strtobool(raw_input("Did you solve it?"))
    f = getFile()
    writeStruggle(inputDate, struggle, reasons, solved)
    
main()
        