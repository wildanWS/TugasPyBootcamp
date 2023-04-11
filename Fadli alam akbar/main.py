print("=== Program Hitung Luas dan Keliling Bangun Datar ===")
print("Pilih Bangun Datar:")
print("                   1. Segitiga")
print("                   2. Lingkaran")
print("                   3. Persegi")
print("                   4. Persegi Panjang")
print("=================================================")

pilihan_bangun = int(input("Masukkan pilihan anda : "))

# LUAS DAN KELILING BANNGUN DATAR SEGITIGA
if pilihan_bangun == 1:
        print("1. Luas")
        print("2. Keliling")
        pilihan_perhitungan = int(input("Masukkan pilihan (1/2): "))
        if pilihan_perhitungan == 1:
            alas = int(input("Masukkan panjang alas: "))
            tinggi = int(input("Masukkan tinggi: "))
            luas = 0.5 * alas * tinggi
            print("Luas segitiga dari alas", alas, "dan tinggi", tinggi, "adalah : ", float(luas))
            print("Terimakasih telah Menggunakan program saya")
        elif pilihan_perhitungan == 2:
            sisi1 = int(input("Masukkan panjang sisi 1: "))
            sisi2 = int(input("Masukkan panjang sisi 2: "))
            sisi3 = int(input("Masukkan panjang sisi 3: "))
            keliling = sisi1 + sisi2 + sisi3
            print("keliling segitiga dari panjang sisi 1,", sisi1, ",sisi 2,", sisi2, "dan sisi 3,", sisi3, "adalah : ", float(keliling))
            print("Terimakasih telah Menggunakan program saya")
        else:
            print("Pilihan tidak sesuai")

# LUAS DAN KELILING BANGUN DATAR LINGKARAN
elif pilihan_bangun == 2:
        print("1. Luas")
        print("2. Keliling")
        pilihan_perhitungan = int(input("Masukkan pilihan anda: "))
        if pilihan_perhitungan == 1:
            radius = int(input("Masukkan nilai jari - jari : "))
            ph1 = 3.14
            luas = ph1 * radius * radius
            print("Luas dari lingkaran dengan jari - jari ", radius, "adalah", float(luas))
            print("Terimakasih telah Menggunakan program saya")
        elif pilihan_perhitungan == 2:
            radius = int(input("Masukkan nilai jari - jari: "))
            keliling = 2 * 3.14 * radius
            print("Keliling dari lingkaran dengan jari - jari ", radius, "aadalah", float(keliling))
            print("Terimakasih telah Menggunakan program saya")
        else:
            print("Pilihan tidak sesuai")

# LUAS DAN KELILING BANGUN DATAR PERSEGI
elif pilihan_bangun == 3:
        print("1. Luas")
        print("2. Keliling")
        pilihan_perhitungan = int(input("Masukkan pilihan anda: "))
        if pilihan_perhitungan == 1:
            sisi = int(input("Masukkan panjang sisi: "))
            luas = sisi * sisi
            print("Luas dari persegi dengan sisi ", sisi, "adalah : ", float(luas))
            print("Terimakasih telah Menggunakan program saya")
        elif pilihan_perhitungan == 2:
            sisi = int(input("Masukkan panjang sisi: "))
            keliling = 4 * sisi
            print("Keliling dari persegi dengan sisi", sisi, "adalah : ", float(keliling))
            print("Terimakasih telah Menggunakan program saya")
        else:
            print("Pilihan tidak sesuai")

# LUAS DAN KELILING BANGUN DATAR PERSEGI PANJANG
elif pilihan_bangun == 4:
        print("1. Luas")
        print("2. Keliling")
        pilihan_perhitungan = int(input("Masukkan pilihan (1/2): "))
        if pilihan_perhitungan == 1:
            panjang = int(input("Masukkan panjang: "))
            lebar = int(input("Masukkan lebar: "))
            luas = panjang * lebar
            print("Luas persegi panjang dari panjang", panjang, "dan lebar", lebar, "adalah : ", float(luas))
            print("Terimakasih telah Menggunakan program saya")
        elif pilihan_perhitungan == 2:
            panjang = int(input("Masukan panjang: "))
            lebar = int(input("Masukan lebar : "))
            keliling = 2 * panjang * lebar
            print("Keliling Persegi panjang dari panjang", panjang, "dan lebar", lebar, "adalah : ", float(keliling))
            print("Terimakasih telah Menggunakan program saya")
        else:
            print("Pilihan tidak sesuai")
else:
     print("Pilihan tidak sesuai")