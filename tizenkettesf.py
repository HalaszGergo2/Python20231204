def tizenkettesf():
    adatokListaja = []
    beFile = open("fileok/allas.txt", "r", encoding="UTF-8")
    for sor in beFile:
        daraboltSor = sor.strip().split("  ")
        # print(daraboltSor)
        adatokListaja.extend(daraboltSor)
    beFile.close()

    db = 0

    index = 0
    while index < len(adatokListaja):
        if adatokListaja[index] == "0":
            db += 1
        index += 1

    print(f"A ledöntött bábuk száma: {db}")