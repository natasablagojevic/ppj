import sys

prelazi = {
    ("ABC", "a"): "ABC", ("ABC", "b"): "ABC"
}

pocetno = "ABC"
zavrsno = ["ABC"]

stanje = pocetno

while True:
    try:
        c = input("Unesi slovo:\n")
        
        if c != "a" and c != "b":
            raise ValueError("Slovo nije deo alfabeta")
    except EOFError:
        break
    except ValueError as err:
        print(err)
        sys.exit()

    if prelazi.get((stanje, c)) is None:
        print("Rec nije deo jezika")
        sys.exit()
    
    stanje = prelazi[(stanje, c)]
    print("\t", stanje)

if stanje in zavrsno:
    print("Rec je deo jezika")
else:
    print("Rec nije deo jezika1")