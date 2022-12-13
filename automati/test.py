import sys

#   (a|b)*a(a|b)
#       |   a   |   b   |
#   ---------------------
#   AC  |   B   |   AC  |
#   B   |   D   |   E   |
#   D   |   D   |   E   |
#   E   |   B   |   AC  |

prelazi = {
    ("AC", "a"): "B", ("AC", "b"): "AC",
    ("B", "a"): "D", ("B", "b"): "E",
    ("D", "a"): "D", ("D", "b"): "E",
    ("E", "a"): "B", ("E", "b"): "AC"
}

#   AC - pocetno
#   D, E - zavrsno

pocetno = "AC"
zavrsna = ["D", "E"]

stanje = pocetno

while True:
    try:
        c = input("Unesi slovo:\n")
        
        if c != "a" and c != "b":
            raise ValueError("Slovo nije deo alfabeta")
        
    except EOFError:
        break
    except ValueError as error:
        print(error)
        sys.exit()
        
    if prelazi.get((stanje, c)) is None:
        print("Rec nije deo jezika")
    
    stanje = prelazi[(stanje, c)]
    print("\t", stanje)
    
if stanje in zavrsna:
    print("Rec je deo jezika")
else:
    print("Rec nije deo jezika")