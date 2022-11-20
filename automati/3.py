import sys

prelazi = {
    ("ADE", "a"): "B", ("ADE", "b"): "C", ("ADE", "c"): "ADE",
    ("B", "b"): "ADE",
}

pocetno = "ADE"
zavrsna = ["C"]

stanje = pocetno

while True:
    try:
        c = input("Unesi slovo\n")
        
        if c != "a" and c != "b" and c != "c":
            raise ValueError("slovo nije deo jezika")
        
    except EOFError:
        break
    except ValueError as err:
        print(err)
        sys.exit()

    if prelazi.get((stanje, c)) is None:
        print("Rec nije deo jezika")
        sys.exit()

    stanje = prelazi[(stanje, c)]
    print("\t", stanje )

if stanje in zavrsna:
    print("Rec je deo jezika")
else:
    print("Rec nije deo jezika")