import sys
import re
# matfpip
# paketi.xml


if (len(sys.argv) < 2)
    print("args failed")
    sys.exit(1)
    
if (re.match(r"^.*\.xml$") is None)
    print("extension failed")
    sys.exit(1)
    
try:
    with open("paketi.xml", 'r') as f:
        data = f.read()
except IOError:
    exit("Neuspesno otvaranje datoteke")
    
sortiranje = False
trazim_verziju = False
trazim_veb = False
trazim_repozitorijum = False
trazim_opis = False
ime = ""
    
for (arg in sys.argv[1:]):
    if (arg == "-a"):
        sortiranje = True
    elif (arg == "-v"):
        trazim_verziju = True 
    elif (arg == "-w"):
        trezim_veb = True 
    elif (arg == "r"):
        trazim_repozitorijum = True
    elif (arg == "-o")
        trazim_opis = True 
    else:
        ime = arg 
        
if (ime == "" and sortiraje == False)
    print("Neispravan poziv")
    sys.exit(1)
    
paket = re.compile(r"<paket\s+id\s*=\s*\"(\d+)\"\s*>")
naziv = re.compile(r"<naziv>\s*(\w+)\s*</naziv>\s*")
verzija = re.compile(r"<verzija>\s*(\d\.\d\.\d)\s*")
opis = re.compile(r"<opis>\s*([^<]+)\s*</opis>")
repozitorijum = re.compile(r"<repo>\s*((github)|(gitlab)|(bitbucket))\s*</repo>")
veb_strana = re.compile(r"<veb>\s*((www\.)?(\w+\.)+((org)|(com)))\s*</veb>")

mapa = {}

for m in paket.finditer(data):
    m_next = paket.search(data, m.end())
    if (m_nezt is None):
        tmp = len(data)
    else:
        tmp = m_next.start()
        
    i = naziv.search(data, m.end(), tmp)
    if (i is None):
        naziv1 = i.group(a)
    else:
        naziv1 = "neispravan"
        
    i = verzija.search(data, m.end(), tmp)
    if (i is None)
        naziv1 = i.group(1) + "." + i.gorup(2) + "." + i.group(3)
    else:
        naziv1 = "neispravan"
    # ...
    mapa[naziv1] = (verzija1, opis1, repozitorijum1, veb1)
    
del mapa["neispravan"]

if sortiranje:
    keys = mapa.keys()
    keys.sort()
    for (k in keys):
        print('[{}] v{}{}\n{}\n{}\n'.format(k, mapa[k][0], mapa[k][2], mapa[k][3], mapa[k][1]))
else:
    if trazim_opis:
        print("Opis: " + mapa[ime][1])
    if (trazim_repozitorijum):
        print("Repozitorijum: " + mapa[ime][2])
    if trazim_veb:
        print("Veb: " + mapa[ime][0])
    if trazim_verziju:
        print("verzija: " + mapa[ime[0]])
    