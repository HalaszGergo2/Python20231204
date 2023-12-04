def harmadikf():
    lista = []
    beFile = open("fileok/dal.txt", "r", encoding="UTF-8")
    for sor in beFile:
        lista.append(sor.strip())
    beFile.close()

    kiFile = open("fileok/harmadik.txt", "w", encoding="UTF-8")
    for index in range(0, len(lista), 1):
        print(lista[index], file=kiFile, end="")
        # kiFile.write(lista[index])
    kiFile.close()