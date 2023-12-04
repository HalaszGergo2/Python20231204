class Szamitogep:


    def __init__(self, szabadmemoria: float, bekapcsolva: bool ):
        if szabadmemoria == 0:
            self.szabadmemoria = 1024
        else:
            self.szabadmemoria = szabadmemoria
        if bekapcsolva == 0:
            self.bekapcsolva = False
        else:
            self.bekapcsolva = bekapcsolva

    def kapcsol(self):
        if self.bekapcsolva:
            self.bekapcsolva = False
        else:
            self.bekapcsolva = True

    def programMasol(self, meret: float) -> bool:
        sikeres = False
        if self.bekapcsolva and self.szabadmemoria - meret > 0:
            self.szabadmemoria -= meret
            sikeres = True
        return sikeres

    def __str__(self):
        if self.bekapcsolva:
            szoveg = "Bekapcsolva"
        else:
            szoveg = "Kikapcsolva"
        return f"Szabad méret: {self.szabadmemoria}, állapot: {szoveg}"


