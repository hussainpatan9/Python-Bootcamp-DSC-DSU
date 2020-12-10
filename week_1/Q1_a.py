
def printdiag(name):
    length=len(name)
    print(f"{length}")
    for i,v in enumerate(name):
        print(" "*(length-i) + f"{v}")


name = input("Name:")
printdiag(name)