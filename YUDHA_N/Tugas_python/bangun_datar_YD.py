# Program menghitung luas dan keliling bangun datar

# Fungsi menghitung luas segitiga
def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Fungsi menghitung keliling segitiga
def hitung_keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

# Fungsi menghitung luas lingkaran
def hitung_luas_lingkaran(jari_jari):
    return 3.14 * (jari_jari ** 2)

# Fungsi menghitung keliling lingkaran
def hitung_keliling_lingkaran(jari_jari):
    return 2 * 3.14 * jari_jari

# Fungsi menghitung luas persegi
def hitung_luas_persegi(sisi):
    return sisi * sisi

# Fungsi menghitung keliling persegi
def hitung_keliling_persegi(sisi):
    return 4 * sisi

# Fungsi menghitung luas persegi panjang
def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Fungsi menghitung keliling persegi panjang
def hitung_keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

# Menampilkan menu
print("Program Menghitung Luas dan Keliling Bangun Datar")
print("1. Segitiga")
print("2. Lingkaran")
print("3. Persegi")
print("4. Persegi Panjang")

# Meminta input dari pengguna
pilihan_bangun = int(input("Masukkan pilihan bangun datar (1-4): "))

# Percabangan untuk memilih bangun datar
if pilihan_bangun == 1:
    print("1. Luas")
    print("2. Keliling")
    pilihan_perhitungan = int(input("Masukkan pilihan perhitungan (1-2): "))
    if pilihan_perhitungan == 1:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = hitung_luas_segitiga(alas, tinggi)
        print("Luas segitiga: ", luas)
    elif pilihan_perhitungan == 2:
        sisi1 = float(input("Masukkan panjang sisi 1: "))
        sisi2 = float(input("Masukkan panjang sisi 2: "))
        sisi3 = float(input("Masukkan panjang sisi 3: "))
        keliling = hitung_keliling_segitiga(sisi1, sisi2, sisi3)
        print("Keliling segitiga: ", keliling)
    else:
        print("Pilihan tidak sesuai")
elif pilihan_bangun == 2:
    print("1. Luas")
    print("2. Keliling")
    pilihan_perhitungan = int(input("Masukkan pilihan perhitungan (1-2): "))
    if pilihan_perhitungan == 1:
        jari_jari = float(input("Masukkan panjang jari-jari: "))
        luas = hitung_luas_lingkaran(jari_jari)
        print("Luas lingkaran: ", luas)
    elif pilihan_perhitungan == 2:
        jari_jari = float(input("Masukkan panjang jari-jari: "))
        keliling = hitung_keliling_lingkaran(jari_jari)
        print("Keliling lingkaran: ", keliling)
    else:
        print("Pilihan tidak sesuai")
elif pilihan_bangun == 3:
    print("1. Luas")
    print("2. Keliling")
    pilihan_perhitungan = int(input("Masukkan pilihan perhitungan (1-2): "))
    if pilihan_perhitungan == 1:
        sisi = float(input("Masukkan panjang sisi: "))
        luas = hitung_luas_persegi(sisi)
        print("Luas persegi: ", luas)
    elif pilihan_perhitungan == 2:
        sisi = float(input("Masukkan panjang sisi: "))
        keliling = hitung_keliling_persegi(sisi)
        print("Keliling persegi: ", keliling)
    else:
        print("Pilihan tidak sesuai")
elif pilihan_bangun == 4:
    print("1. Luas")
    print("2. Keliling")
    pilihan_perhitungan = int(input("Masukkan pilihan perhitungan (1-2): "))
    if pilihan_perhitungan == 1:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = hitung_luas_persegi_panjang(panjang, lebar)
        print("Luas persegi panjang: ", luas)
    elif pilihan_perhitungan == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        keliling = hitung_keliling_persegi_panjang(panjang, lebar)
        print("Keliling persegi panjang: ", keliling)
    else:
        print("Pilihan tidak sesuai")
else:
    print("Pilihan tidak sesuai")


    #NAMA : YUDHA NIRWANA

