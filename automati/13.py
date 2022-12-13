import sys

prelazi = {
    ("AEF", "a"): "BD", ("AEF", "b"): "C",
    ("BD", "a"): "BD", ("BD", "b"): "AEF",
    ("C", "a"): "AEF", ("C", "b"): "C"
}

pocetno = "AEF"
zavrsna = ["AEF", "BD"]

stanje = pocetno

while True:
    try:
        c = input("Unesi slovo\n")
        if c != "a" and c != "b":
            raise ValueError("Nije deo alfabeta")
    except EOFError:
        break
    except ValueError as err:
        print(err)
        sys.exit()
        
    if prelazi.get((stanje, c)) is None:
        print("Nije deo jez")
        sys.exit()
        
    stanje = prelazi[(stanje, c)]
    print("\t", stanje)
    
if stanje in zavrsna:
    print("Rec je deo jezika")
else:
    print("Rec nije deo jezika")