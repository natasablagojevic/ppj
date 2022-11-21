import sys

#       |   a   |   b   |
#   ---------------------
#   AC  |   B   |   AC  |
#   B   |   D   |   AC  |
#   D   |   D   |   E   |
#   E   |   B   |   AC  |

prelazi = {
    ("AC", "a"): "B", ("AC", "b"): "AC",
    ("B", "a"): "D", ("B", "b"): "AC",
    ("D", "a"): "D", ("D", "b"): "E",
    ("E", "a"): "B", ("E", "b"): "AC"
}

pocetno = "AC"
zavrsna = ["E"]

stanje = pocetno

while True:
    try:
        c = input("Unesi slovo\n")
        if c != "a" and c != "b":
            raise ValueError("slovo nije deo alfabeta")
    except EOFError:
        break
    except ValueError as err:
        print(err)
        sys.exit()
        
    if prelazi.get((stanje, c)) is None:
        print("Nije deo alfabeta")
        sys.exit()
        
    stanje = prelazi[(stanje, c)]
    print("\t", stanje)
    
if stanje in zavrsna:
    print("Rec je deo jezika")
else:
    print("Rec nije deo jezika")