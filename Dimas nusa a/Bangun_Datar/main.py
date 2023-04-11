print("Selamat datang di program bangun datar")
print("======================================")
print("Pilih bangun datar:")
print("          1.Segitiga")
print("          2.Lingkaran")
print("          3.Persegi")
print("          4.Persegi Panjang")
print("          5.Keluar Program")

pilihan = int(input("Masukan pilihan:"))

if pilihan == 1:
    
    print("Pilih salah satu: ")
    print("        1.Luas Segitiga")
    print("        2.Keliling Segitiga")
     
    pilih = int(input("Masukan pilihan: "))
    if pilih == 1:
        print("Menghitung Luas Segetiga ")
        print("=========================")
        a = int(input("Masukan alas: "))
        t = int(input("Masukan tinggi: "))
        luas = 0.5*a*t
        print("=========================")
        print("Luas segitiga dari alas",a,"cm tinggi",t,"cm adalah: ",str(luas))
        print("Terimakasih Telah Menggunakan Program Saya :)")

    elif pilih == 2:
        print("Menghitung Keliling Segitiga")
        print("=============================")
        a = int(input("Masukan alas: "))
        keliling = a+a+a
        print("=========================")
        print("Keliling segitiga dari",a,"adalah: ",str(keliling))
        print("Terimakasih Telah Menggunakan Program Saya :)")

    else:
        print("Error : Input angka yang sesuai..")


elif pilihan == 2:

    print("Pilih salah satu: ")
    print("        1.Luas Lingkaran")
    print("        2.Keliling Lingkaran")

    pilih = int(input("Masukan pilihan: "))
    if pilih == 1:
        print("Menghitung Luas Lingkaran")
        print("=========================")

        r = float(input("Masukan Jari-Jari: "))

        phi = 3.14

        luas = phi*r*r
        print("=========================")
        print("Luas Lingkaran adalah: ", str("%.2f" % luas))
        print("Terimakasih Telah Menggunakan Program Saya :)")

    elif pilih == 2:
        print("Menghitung Keliling Lingkaran")
        print("=========================")

        r = float(input("Masukan Jari-Jari: "))

        phi = 3.14
        diameter = 2*r

        keliling = phi*diameter
        print("=========================")
        print("Keliling Lingkaran Adalah: ",str("%.2f" % keliling))
        print("Terimakasih Telah Menggunakan Program Saya :)")

    else:
        print("Error : Input angka yang sesuai..")


elif pilihan == 3:

    print("Pilih salah satu: ")
    print("        1.Luas Persegi")
    print("        2.Keliling Persegi")

    pilih = int(input("Masukan pilihan: "))

    if pilih == 1:
        print("Menghitung Luas Persegi")
        print("=========================")

        s=float(input("Masukan nilai sisi: "))
        l =s*s

        print("=========================")
        print("Luasn persegi: ", l)
        print("Terimakasih Telah Menggunakan Program Saya :)")

    elif pilih == 2:
        print("Menghitung Keliling Persegi")
        print("=========================")

        s=float(input("Masukan nilai sisi: "))

        k = 4*s

        print("=========================")
        print("Keliling persegi dari", k)
        print("Terimakasih Telah Menggunakan Program Saya :)")

    else:
        print("Error : Input angka yang sesuai..")



elif pilihan == 4:

    print("Pilih salah satu: ")
    print("        1.Luas Persegi Panjang")
    print("        2.Keliling Persegi panjang")

    pilih = int(input("Masukan pilihan: "))

    if pilih == 1:
        print("Menghitung Luas Persegi panjang")
        print("=========================")

        p = int(input("Masukan nilai panjang: "))
        l = int(input("Masukan nilai lebar: "))

        luas = p*l

        print("=========================")
        print("Luas persegi panjang adalah: ",str (luas))
        print("Terimakasih Telah Menggunakan Program Saya :)")
    
    elif pilih == 2:
        print("Menghitung Keliling Persegi panjang")
        print("=========================")

        p = int(input("Masukan nilai panjang: "))
        l = int(input("Masukan nilai lebar: "))

        keliling = 2*(p+l)

        print("=========================")
        print("Keliling persegi panjang adalah ", str(keliling))
        print("Terimakasih Telah Menggunakan Program Saya :)")

    
    else:
        print("Error : Input angka yang sesuai..")



elif pilihan == 5:
    print("")

else:
    print("Error : Input angka yang sesuai..")