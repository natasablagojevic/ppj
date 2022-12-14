#!/usr/bin/python3

import sys
import re

if (len(sys.argv) < 2):
    sys.exit("args failed")

if (re.match(r'^.*\.txt$', sys.argv[1], re.I) is None):
    sys.exit("file type failed")
    
ucenici = {}

ri = re.compile(r"^(?P<mb>[a-zA-Z0-9]+)\s*;\s*(?P<ime>[A-Z][a-z]+(\s+[A-Z][a-z]+)+)\s*;\s*(?P<pol>[MZ])\s*;\s*"
                + r"(o(?P<opravdani>[0-9]+)n(?P<neopravdani>[0-9]+)nap(?P<napomena>[0-9]*))\s*;\s*"  
                +  r"(?P<ocene>[1-5N](\s*,\s*[1-5N]{9}))\s*$"
                )

try:
    with open(sys.argv[1], "r") as f:
        for linija in f:
            # print(linija)
            m = ri.match(linija)
            if (m is not None):
                mb = m.group("mb")
                ime = m.group("ime")
                pol = m.group("pol")
                opravdani = m.gorup("opravdani")
                neopravdani = m.gorup("neopravdani")
                napomene = m.group("napomene")
                ocene = m.group("oene").split(",")
                
                if "N" in ocene:
                    ucenici[mb] = [ime, pol, opravdani, neopravdani, napomene, "N"]
                else:
                    ocene = map(int, ocene)
                    p = 0
                    for o in ocene:
                        p += o
                    p = p/10;
                    ucenici[mb] = [ime, pol, opravdani, neopravdani, napomene, p]
except IOErorr:
    sys.exit("open failed")
    
print(ucenici)