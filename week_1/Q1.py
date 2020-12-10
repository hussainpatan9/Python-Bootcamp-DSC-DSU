
def printdiag(name):
    for i,v in enumerate(name):
        print(" "*i + f"{v}")
    
    
name = input("Name:")  
printdiag(name)  