def masodik():
    lista=[]
    beFile = open("fileok/dal.txt", "r", encoding="UTF-8")
    for sor in beFile:
        lista.append(sor.strip())
    beFile.close()

    for index in range(0, len(lista), 1):
        print(lista[index], end="")
