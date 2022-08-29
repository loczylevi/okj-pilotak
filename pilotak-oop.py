#név;    születési_dátum;      nemzetiség;       rajtszám
class Pilotak:
    def __init__(self,sor):
        nev,szuletes,nemzet,rajtszam = sor.strip().split(";")
        self.nev = nev
        self.szuletes = szuletes
        self.nemzet = nemzet
        self.rajtszam = rajtszam
        self.ev = int(szuletes[0:4])
             
with open("pilotak.csv","r",encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [Pilotak(sor) for sor in f]
    
print(f"3.feladat: {len(lista)}")

utolso_pilota = [sor.nev for sor in lista][-1]

print(f"4.feladat: {utolso_pilota}")

pilotak_19_szazad = [sor for sor in lista if sor.ev < 1901]

print("5.feladat:")
[print(f"       {sor.nev} ({sor.szuletes})") for sor in pilotak_19_szazad]

rajtszamok = [(int(sor.rajtszam),sor) for sor in lista if sor.rajtszam != ""]

legkisebb, adat = min(rajtszamok)

print(f"6.feladat: {adat.nemzet}")

#7.feladat
rajtszam2 = [int(sor.rajtszam) for sor in lista if sor.rajtszam != ""]

statisztika = dict()
print("7.feladat:",end="")
for sor in rajtszam2:
    rajtszam = sor
    statisztika[rajtszam] = statisztika.get(rajtszam, 0) + 1
tobb_azonos_rajtszam = [ print(f' {rajtszam},',end="") for rajtszam, db in statisztika.items() if db > 1]