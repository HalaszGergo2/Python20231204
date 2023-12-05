def osztalyBeir():
    kiFile = open("fileok/proba.txt", "a", encoding="UTF-8")
    kiFile.write("\ndiák")
    kiFile.close()
def kiir():
    beFile = open("fileok/proba.txt", "r", encoding="UTF-8")
    adatok = beFile.read()
    print(adatok)
    beFile.close()

# második sor
    beFile = open("fileok/proba.txt", "r", encoding="UTF-8")
    beFile.readline()
    print(beFile.readline())
    beFile.close()

# első 5 karatker
    beFile = open("fileok/proba.txt", "r", encoding="UTF-8")
    elso5 = beFile.read(5)
    print(elso5)
    beFile.close()
    
