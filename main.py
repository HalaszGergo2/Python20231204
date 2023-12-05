"""
import Szamitogep
import elsof
import f1
import f2
import harmadikf
import hetedikf
import masodikf
import negyedikf
import nyolcadikf
import tizenkettesf
"""
import Csoport

"""
szg1 = Szamitogep.Szamitogep(0, False)
szg2 = Szamitogep.Szamitogep(0, False)

szg1.kapcsol()
if szg1.programMasol(800):
    print("A másolás sikeres volt")
else:
    print("A másolás sikertelen volt")
if szg1.programMasol(400):
    print("A másolás sikeres volt")
else:
    print("A másolás sikertelen volt")

if szg2.programMasol(1):
    print("A másolás sikeres volt")
else:
    print("A másolás sikertelen volt")

print(szg1)
print(szg2)
"""

# elsof.elso()
# masodikf.masodik()
# harmadikf.harmadikf()
# negyedikf.negyedikf()
# hetedikf.hetedikf()
# nyolcadikf.nyolcadikf()
# tizenkettesf.tizenkettesf()
# f1.Osztalybeir()
# f1.kiir()
# f2.masodik()

adatokLista = []
def beolvasas():
    beFile = open("fileok/osztaly.txt", "r", encoding="UTF-8")
    # első sor
    beFile.readline()
    # többi sor
    sorok = beFile.readlines()
    for sor in sorok:
        # adat tisztitása
        tisztitottsor = sor.strip()
        # darabolás
        daraboltsor = tisztitottsor.split("/")
        csoporttag = Csoport.Csoport(daraboltsor[0], daraboltsor[1], daraboltsor[2])
        print(csoporttag)
        # belefűzöm az objektumot a listába
        adatokLista.append(csoporttag)
    beFile.close()

def sorokszama():
    sorszam = len(adatokLista)
    print(f"A tanulók száma: {sorszam}.")

def megszamlalas():
    osszeg = 0
    for index in range(0, len(adatokLista), 1):
        osszeg += adatokLista[index].atlag

    if len(adatokLista) == 0:
        atlag = 0
    else:
        atlag = osszeg/len(adatokLista)
    print(f"Az suli átlag: {atlag}")

def elsos():
    elsos = 0
    for index in range(0, len(adatokLista), 1):
        if adatokLista[index].evfolyam == 1:
            elsos += 1
    print(f"Az elsősök száma: {elsos}")


beolvasas()
sorokszama()
megszamlalas()
elsos()