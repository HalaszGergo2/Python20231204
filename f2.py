def masodik():
    beFile = open("fileok/masodik.txt", "r", encoding="UTF-8")
    beFile.readline()
    print(beFile.readline())
    beFile.close()

    # 4. sor beirasa

    beFile = open("fileok/masodik.txt", "a", encoding="UTF-8")
    beFile.write("\nnegyedik sor")
    beFile.close()

    # teljes file kiiratása
    beFile = open("fileok/masodik.txt", "r", encoding="UTF-8")
    print(beFile.read())
    beFile.close()