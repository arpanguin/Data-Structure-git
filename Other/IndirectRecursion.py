def calculateA(n):
    if n > 0:
        print("Arpan")
        ...
        calculateB(n - 1)
        ...


def calculateB(n):
    if n > 0:
        print("Guin")
        ...
        calculateA(n - 1)
        ...


calculateA(3)


