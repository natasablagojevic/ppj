#!/usr/bin/python3

import sys
import re 


# RB/NAZIVTEL-DIJAGONALA"/RAM/POVEZIVANJE/KORISCENJE

reg_exp = r"^\s*(?P<rb>(\d)+)\s*\/"
reg_exp += r"(?P<ime>[a-zA-Z0-9]+(\s+[a-zA-Z0-9]+)+)\s*(?P<dijag>([0-9]+[,])?[0-9]+)\"\s*\/"
reg_exp += r"(?P<ram>(\d)+\s*((GB)|(GigaByte)|(gigabajt)))\s*\/"
reg_exp += r"(?P<povezivanje>((WiFi)|(HotSpot)|(USB)|(Bluetooth))(\s*,\s*((WiFi)|(HotSpot)|(USB)|(Bluetooth))))\s*\/"
reg_exp += r"(?P<koris>(([a-zA-Z0-9\s]*)(\s*[,a-zA-Z0-9\s]*)))*$"

ri = re.compile(reg_exp)

telefoni = {}

try:
    with open("mobilni.txt", "r") as f:
        for linija in f:
            # print(linija)
            m = ri.match(linija)
            if (m is not None):
                print(m.group())
                rb = m.group("rb")
                ime = m.group("ime")
                dijagonala = m.group("dijag")
                ram = m.group("ram")
                povezivanje = m.group("povezivanje").split(",")
                koriscenje = m.group("koris")

                telefoni[rb] = [ime, dijagonala, ram, povezivanje, koriscenje]
                
        # print(telefoni)
                
except IOError:
    sys.exit("open failed")
    
# keys = list(telefoni)
# keys.sort(reverse=True)
# print(telefoni)