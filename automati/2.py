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
        print("Rec nije deo jezika")
        sys.exit()

    stanje = prelazi[(stanje, c)]
    print("\t", stanje)

if stanje in zvrsna:
    print("Rec je deo alfabeta")
else:
    print("Rec nije deo alfabeta")