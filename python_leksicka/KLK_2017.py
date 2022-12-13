import sys
import re

# igraci.csv -g
#       ili  -t KLUB

if len(sys.argv) < 3:
    exit('args failed')

gol = False
klub = False
naziv = ""

for a in sys.argv[2:]:
    if (a == "-g"):
        gol = True
    elif (a == "-t"):
        klub = True
    elif (klub == True):
        naziv = a
    else:
        print(a)
        exit('Uneta pogresna komanda')
        
if (re.match(r"^.*\.csv$", sys.argv[1]) == None):
    exit('Fajl nije csv')
    
try:
    with open(sys.argv[1]) as f:
        datoteka = f.readlines()
except IOError as e:
    print(e)
    exit(1)
    
igraci = []
                    # ime prezime
reg = re.compile(  r"([A-Z][a-z]+\s*(?:[a-zA-Z]*\s+[A-Z][a-z]*)?)"
                 + r",\s*[A-Z][a-z]+"   #drzava
                 + r",\s*[1-9]+"        # poeni
                 + r",\*s(\d{4}-\d{4})?" #godine
                 + r",\s*([A-Z][a-zA-Z0-9]+[ a-zA-Z0-9]*(?:,\*[A-Z][a-zA-Z0-9]+[ a-zA-Z0-9]*)*)" # klubovi
                 )

for linija in datoteka:
    m = reg.search(linija)
    if m is not None:
        # print(m.groups())
        igraci.append(m.groups())
        
if gol:
    igraci.sort(reverse=True, key= lambda x: int(x[2])/float(x[3]))
    for i in igraci:
        print("%s %.2f", i[0], int(i[2])/float(i[3]))
elif klub:
    for i in igraci:
        if (naziv in i[6]):
            print(i[0], i[4])
            if (i[5] is not None):
                print(int(i[5])-int(i[4]))
            else:
                print(2018 - int(i[4]))
                