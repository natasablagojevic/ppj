import sys

prelazi = {
    ("AC", "a"): "B", ("AC", "b"): "AC",
    ("B", "a"): "B", ("B", "b"): "D",
    ("D", "a"): "B", ("D", "b"): "E",
    ("E", "a"): "B", ("E", "b"): "AC"
}

pocetno = "AC"
zavrsna = ["E"]

stanje = pocetno

while True:
    try:
        c = input("Unesite slovo\n")

        if c != "a" and c != "b":
            raise ValueError("nije deo alfabeta")
    except EOFError:
        break
    except ValueError as err:
        print(err)
        sys.exit()

    if prelazi.get((stanje, c)) is None:
        print("Nije deo jezika")
        sys.exit()
    
    stanje = prelazi[(stanje, c)]
    print("\t", stanje)

if stanje in zavrsna:
    print("Rec je deo jezika")
else:
    print("Rec nije deo jezika")