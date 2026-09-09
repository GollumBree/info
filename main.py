import random


class Biber:
    def __init__(self, name: str, alter: int, elevel: float):
        self.name = name
        self.alter = alter
        self.elevel = elevel
        self.will_schlafen = False

    def ausruhen(self):
        self.elevel = min(self.elevel + 10, 100)
        if self.elevel == 100:
            self.will_schlafen = False
            print(f"{self.name} hat sich AUSGEROOTH")

    def arbeiten(self):
        raise NotImplementedError


class Baumeister(Biber):
    dammfortschritt: int = 0

    def bauen(self):
        if self.elevel >= 20:
            self.elevel -= 20
            self.dammfortschritt += 1
            print(f'Biber "{self.name}" baut einen Damm. ({self.dammfortschritt})')
        else:
            self.will_schlafen = True

    arbeiten = bauen


class Sammler(Biber):
    resourcen: int = 0

    def sammeln(self):
        if self.elevel >= 15:
            self.elevel -= 15
            self.resourcen += (temp := random.randint(1, 10))
            print(f'Biber "{self.name}" sammelt {temp} Resourcen. ({self.resourcen})')
        else:
            self.will_schlafen = True

    arbeiten = sammeln


class Wächter(Biber):
    def patrouillieren(self):
        if self.elevel >= 10:
            self.elevel -= 10
            print(f'Biber "{self.name}" patrouilliert.')
        else:
            self.will_schlafen = True

    arbeiten = patrouillieren


class Biberwelt:
    def __init__(self, *biber: Biber):
        self.biber = list(biber)

    def biber_hinzufügen(self, *biber: Biber):
        self.biber.extend(biber)

    def sim(self):
        for b in self.biber:
            b.arbeiten()
            b.ausruhen()

    def sterben(self):
        self.biber = list(filter(lambda b: b.alter < 2000, self.biber))

    def ausbeuten(self):
        while self.biber:
            for b in self.biber:
                b.alter += 1
                if b.will_schlafen:
                    b.ausruhen()
                else:
                    b.arbeiten()

            if len(self.biber) >= 2 and random.random() >= 0.9:
                ...
            
            self.sterben()
        print("Alle tot.")


welt = Biberwelt(Baumeister("Bob", 99, 100))
welt.biber_hinzufügen(
    Sammler("Butzelmann", 34, 0),
    Wächter("St. Martin", 12, 3),
)

welt.ausbeuten()
