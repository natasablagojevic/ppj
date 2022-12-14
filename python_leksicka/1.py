import sys
import re

if (len(sys.argv) < 2)
    sys.exit("args failed")
    
if (re.match(r"^.*\.xml$", sys.argv[1]) is None):
    sys.exit("type failed")
    
try:
    # with open(sys.argv[1], "r") as f :
    f = open(sys.argv[1], "r")
except IOError:
    sys.exit("open")
    
sortirati = False
verzija = False
veb = False
repo = False
opis = False

for arg in sys.argv[2:]:
    if (arg == "-a"):
        sortirati = True
    if (arg == "-v"):
        verzija = True 
    if (arg == "-w"):
        veb = True 
    if (arg == "-r"):
        repo = True
    if (arg == "-o"):
        opis = True    
    else 
        sys.exit("bad option")
        
ri = re.compile(    r"<paketi\s+id\s*=\s*\"[0-9]+\"\s*>\s*" + 
                    r"<naziv>\s*([a-zA-Z0-9]+)\s*</naziv>" + 
                    r"<verzija>\s*(\d+\.\d+\.\d+)\s*</verzija>" + 
                    r"<opis>\s*([^<]+)\s*</opis>" + 
                    r"<repo>\s*((github)|(gitlab)|(bitbucket))\s*" +
                    r"<veb>\s*((www.)?(\w+\.)+((org)|(com)))\s*</veb>"
                )

mapa = {}

for m in ri.finditer(data):
    if m is not Null:
        m_next = ri.search(data, m.end())
    
    if m_next is None:
        tmp = len(data)