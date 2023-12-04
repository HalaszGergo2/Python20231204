def elso():
    beFile = open("fileok/dal.txt", "r", encoding="UTF-8")
    for sor in beFile:
        print(sor.strip(), end="")
    beFile.close()
