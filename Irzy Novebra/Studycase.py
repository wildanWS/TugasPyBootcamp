print("Selamat Datang Di Program Bangun Datar!")
print("=======================================")
print("1.Segitiga")
print("2.Lingkaran")
print("3.Persegi")
print("4.Persegi Panjang")
print("=======================================")

while True:
    pilihan = int(input("Pilih Salah Satu Menu Di Atas: "))

    if pilihan == 1:
        print("Menghitung Luas dan Keliling Segitiga")
        print("=====================================")

        a = int(input("Masukan Nilai Alasnya: "))
        t = int(input("Masukan Nilai Tingginya: "))

        luas = 0.5*a*t
        keliling = a+a+a

        print("=====================================")
        print("Luas Segitiga Dari Adalah: ", str(luas)) 
        print("Kelilingnya Adalah: ", str(keliling))
        break

    elif pilihan == 2:
        print("Menghitung Luas dan Keliling Lingkaran")
        print("======================================")

        r = float(input("Masukan Nilai Jari-jari: "))

        phi = 3.14
        diameter = 2*r

        luas = phi*r*r
        keliling = phi*diameter

        print("=======================================")
        print("Luasnya Adalah:  ", str("%.2f" % luas))
        print("Kelilingnya Adalah: ", str("%.2f" % keliling))
        break

    elif pilihan == 3:
        print("Menghitung Luas dan Keliling Persegi")
        print("====================================")

        s = int(input("Masukan Nilai Sisinya: "))

        luas = s*s
        keliling = s*s*s*s
        
        print("=====================================")
        print("Luasnya Adalah: ", str(luas))
        print("Kelilingnya Adalah: ", str(keliling))
        break

    elif pilihan == 4:
        print("Menghitung Luas dan Keliling Persegi Panjang")
        print("============================================")

        p = int(input("Masukan Nilai Panjangnya: "))
        l = int(input("Masukan Nilai Lebarnya: "))

        luas = p*l
        keliling = 2*(p+l)

        print("=============================================")
        print("Luasnya Adalah: ", str(luas))
        print("Kelilingnya Adalah: ", str(keliling))
        break

    else:
     print("===================================")
     print("Pilihan Tidak Sesuai!")

