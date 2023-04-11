def luas_segitiga():
    print()
    print("  Menghitung Luas Segitiga  ")
    print("============================")
    als = int(input("Masukkan alas : "))
    tg = int(input("Masukkan tinggi : "))
    luasS = 0.5*int(als*tg)

    print(f"Luas Segitiga dari alas {als} dan tinggi {tg} adalah: {luasS}")
    print()
    print("Thank You for Using Our Program!")

def luas_persegi():
    print()
    print("  Menghitung Luas Persegi  ")
    print("===========================")
    sisi = int(input("Masukkan Sisi: "))
    luasP = int(sisi*sisi)

    print(f"Luas Persegi dari sisi {sisi} adalah:   {luasP}")
    print()
    print("Thank You for Using Our Program!")


def luas_lingkaran():
    print()
    print("  Menghitung Luas Lingkaran  ")
    print("=============================")
    phi = 3.14
    r = int(input("Masukkan jari - jari: "))
    luasL = phi*r*r

    print(f"Luas Lingkaran dari jari jari {r} adalah: {luasL}")
    print()
    print("Thank You for Using Our Program!")

def luas_persegi_panjang():
    print()
    print("  Menghitung Luas Persegi Panjang  ")
    print("===================================")
    p = int(input("Masukkan panjang: "))
    l = int(input("Masukkan lebar: "))
    luasPL = p*l

    print(f"Luas Persegi Panjang dari panjang {p} dan lebar {l} adalah: {luasPL}")
    print()
    print("Thank You for Using Our Program!")


def keliling_segitiga():
    print()
    print("  Menghitung Keliling Segitiga  ")
    print("================================")
    a = int(input("Masukkan sisi a: "))
    b = int(input("Masukkan sisi b: "))
    c = int(input("Masukkan sisi c: "))
    kelS = a + b + c

    print(f"Keliling Segitiga dari sisi a {a}, sisi b{b}, dan sisi c{c} adalah: {kelS}")
    print()
    print("Thank You for Using Our Program!")

def keliling_persegi():
    print()
    print("  Menghitung Keliling Persegi  ")
    print("===============================")
    s = int(input("Masukkan sisi: "))
    kelP = s*4

    print(f"Keliling Persegi dari sisi {s} adalah: {kelP}")
    print()
    print("Thank You for Using Our Program!")

def keliling_persegi_panjang():
    print()
    print("  Menghitung Keliling Persegi Panjang  ")
    print("=======================================")
    P = int(input("Masukkan panjang: "))
    L = int(input("Masukkan lebar: "))
    kelPL = (2*P)+(2*L)

    print(f"Keliling Persegi Panjang dari panjang {P} dan lebar {L} adalah: {kelPL}")
    print()
    print("Thank You for Using Our Program!")

def keliling_lingkaran():
    print()
    print("  Menghitung Keliling Lingkaran  ")
    print("=================================")
    Phi = 3.14
    R = int(input("Masukkan diameter: "))
    kelL = 2*Phi*R

    print(f"Keliling Lingkaran dari jari-jari {R} adalah: {kelL}")
    print()
    print("Thank You for Using Our Program!")