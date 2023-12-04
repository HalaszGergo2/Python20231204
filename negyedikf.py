def negyedikf():
    lista = []
    beFile = open("fileok/dal.txt", "r", encoding="UTF-8")
    for sor in beFile:
        lista.append(sor.strip())
    beFile.close()

    kiFile = open("fileok/negyedik.txt", "w", encoding="UTF-8")
    for index in range(0, len(lista), 1):
        daraboltsor = lista[index].split(" ")
        print(daraboltsor[0], file=kiFile)
        # kiFile.write(lista[index])
    kiFile.close()
