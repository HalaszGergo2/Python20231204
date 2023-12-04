def hetedikf():
    lista = []
    beFile = open("fileok/dal.txt", "r", encoding="UTF-8")
    for sor in beFile:
        lista.append(sor.strip())
    beFile.close()

    kiFile = open("fileok/hetedik.txt", "w", encoding="UTF-8")
    for index in range(len(lista)-1, -1, -1):
        print(lista[index])
        print(lista[index], file=kiFile)
    kiFile.close()