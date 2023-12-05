def nyolcadikf():
    beFile = open("fileok/dal.txt", "r", encoding="UTF-8")
    fileTartalma = beFile.read()
    # print(type(fileTartalma))
    # print(fileTartalma)
    beFile.close()
    dbk = 0
    dbK = 0
    fileTartalmaUj = ""
    for index in range(0, len(fileTartalma), 1):
        if fileTartalma[index] == "k":
            dbk += 1
            fileTartalmaUj += "*"
        elif fileTartalma[index] == "K":
            dbK += 1
            fileTartalmaUj += "*"
        else:
            fileTartalmaUj += fileTartalma[index]
    print(f"Cenzúrázott file tartalma: {fileTartalmaUj}")
    print(f"k betűk száma: {dbk}, K betűk száma {dbK}")
