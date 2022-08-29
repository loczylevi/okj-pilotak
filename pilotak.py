#név;    születési_dátum;      nemzetiség;       rajtszám
             
with open("pilotak.csv","r",encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [sor.strip().split(";") for sor in f]
    
print(f"3.feladat: {len(lista)}")

utolso_pilota = [sor[0] for sor in lista][-1]

print(f"4.feladat: {utolso_pilota}")

pilotak_19_szazad = [sor for sor in lista if int(sor[1][0:4]) < 1901]

print("5.feladat:")
[print(f"       {sor[0]} ({sor[1]})") for sor in pilotak_19_szazad]

rajtszamok = [(int(sor[3]),sor) for sor in lista if sor[3] != ""]

legkisebb, adat = min(rajtszamok)

print(f"6.feladat: {adat[2]}")

#7.feladat
rajtszam2 = [int(sor[3]) for sor in lista if sor[3] != ""]

statisztika = dict()
print("7.feladat:",end="")
for sor in rajtszam2:
    rajtszam = sor
    statisztika[rajtszam] = statisztika.get(rajtszam, 0) + 1
tobb_azonos_rajtszam = [ print(f' {rajtszam},',end="") for rajtszam, db in statisztika.items() if db > 1]
