def luasSegitiga():
    print(" Menghitung luas segitiga ")
    print("==========================")

    alas = int(input('Masukan Alas : '))
    tinggi = int(input('Masukan Tinggi : '))

    luas = (alas * tinggi) /2

    print("=============================================================")
    print(f"Luas segitiga dari alas {alas} tinggi {tinggi} adalah {luas}")
    print("Terima kasih telah menggunakan program saya :)")

def kelilingSegitiga():
    print(" Menghitung keliling segitiga ")
    print("==========================")

    s = int(input('Masukan sisi : '))
    ss = int(input('Masukan sisi : '))
    sisi = int(input('Masukan sisi : '))

    luas = (s + ss + sisi)

    print("====================================================================")
    print(f"Keliling segitiga dari sisi {s} sisi {ss} sisi {sisi} adalah {luas}")
    print("Terima kasih telah menggunakan program saya :)")

def luasLingkaran():
    print(" Menghitung luas lingkaran ")
    print("==========================")

    jari_jari = int(input('Masukan panjang jari-jari : '))

    luas = (3.14 * jari_jari * jari_jari)

    print("================================================================")
    print(f"Luas lingkaran dari panjang jari-jari {jari_jari} adalah {luas}")
    print("Terima kasih telah menggunakan program saya :)")

def kelilingLingkaran():
    print(" Menghitung keliling lingkaran ")
    print("==========================")

    jari_jari = int(input('Masukan panjang jari-jari : '))
    π = 3.14

    luas = (2 * π * jari_jari)

    print("====================================================================")
    print(f"keliling lingkaran dari panjang jari-jari {jari_jari} adalah {luas}")
    print("Terima kasih telah menggunakan program saya :)")


def luasPersegi():
    print(" Menghitung luas persegi ")
    print("==========================")

    sisiP = int(input('Masukan sisi persegi :'))

    luas = (sisiP * sisiP)

    print("================================================================")
    print(f"Luas persegi dari sisi persegi {sisiP} adalah {luas}")
    print("Terima kasih telah menggunakan program saya :)")

def kelilingPersegi():
    print(" Menghitung keliling persegi ")
    print("==========================")

    sisiP = int(input('Masukan sisi persegi : '))

    luas = (4 * sisiP)

    print("================================================================")
    print(f"Keliling persegi dari sisi persegi {sisiP} adalah {luas}")
    print("Terima kasih telah menggunakan program saya :)")

def luasPersegiPanjang():
    print(" Menghitung luas perseg panjang ")
    print("==========================")

    panjang = int(input('Masukan panjang persegi : '))
    lebar = int(input('Masukan lebar persegi : '))

    luas = (panjang * lebar)

    print("===================================================================")
    print(f"Luas persegi panjang dari panjang {panjang} lebar {lebar} adalah {luas}")
    print("Terima kasih telah menggunakan program saya :)")

def kelilingPersegiPanjang():
    print(" Menghitung keliling persegi panjnag ")
    print("==========================")

    panjang = int(input('Masukan panjang persegi : '))
    lebar = int(input('Masukan lebar persegi : '))

    luas = (2 * panjang) + (2 * lebar)

    print("===================================================================")
    print(f"Keliling persegi panjang dari panjang {panjang} lebar {lebar} adalah {luas}")
    print("Terima kasih telah menggunakan program saya :)")