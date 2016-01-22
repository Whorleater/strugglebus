#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os.path
from datetime import date
from distutils import util

class struggle(object):
    """Struggle Object
    Class Variables:
        file: str, location of the journal file
    Instance Variables:
        date: str, date of entry (isoformat)
        info:  str, answer to 'What was today's biggest struggle?'
        reasons:  str, answer to 'Why?'
        solved: bool, answer to 'solved?'
    """
    def __init__(self, customFilename = ""):
        super(struggle, self).__init__()
        self.info = ""
        self.reasons = ""
        self.solved = ""
        if not customFilename:
            self.file = "strugglebus.json"
        else:
            self.file = customFilename
        self.findFile()
    pass
    
    def findFile(self):
        """finds the file, if it doesn't exist, then create one"""
        if not os.path.isfile(self.file):
            with open(self.file, "w+") as journalFile:
                strugglebus = {}
                journalFile.write(json.dumps(strugglebus))
    pass
        
    def write(self, info, reasons, solved, date = date.today().isoformat()):
        """takes the date, info, reasons, and solved and writes them to the json"""
        journal = {}
        with open(self.file, "r") as journalFile:
            journal = json.load(journalFile)
        with open(self.file, "w+") as journalFile:
            entry = {"date": date, "biggestStruggle" : info, "why" : reasons, "solved" : solved}
            entryNum = int(sorted(journal.keys())[-1]) + 1 if len(journal.keys()) > 0 else 1
            journal[str(entryNum)] = entry
            journalFile.write(json.dumps(journal, ensure_ascii=True, indent = 4))
    pass
        
        


def main():
    journal = struggle()
    info = raw_input("What was today's biggest struggle?\n")
    reasons = raw_input("Why did you have that struggle?\n")
    solved = util.strtobool(raw_input("Did you solve it?\n"))
    journal.write(info, reasons, solved)
    
main()
        