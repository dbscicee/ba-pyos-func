def printnumber():
    names = ["Aala", "bala", "cala", "dala", "eala", "fala"]
    ages = [10, 20, 30, 50, 32, 65]
    for name in names:
        print(name)
        if name == "bala":
            print("--- "+name)
            break
        else:
            print("not matching")
