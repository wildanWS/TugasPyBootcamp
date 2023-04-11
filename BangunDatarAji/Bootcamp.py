def Segitiga():
    while True:
        print("===Anda Telah Memilih Segitiga===")
        print("1. Luas Segitiga")
        print("2. Keliling Segitiga")
        print("0. Keluar")
        pilihan = input("Masukan pilihan :")
        if pilihan == "1":
            print("===Luas Segitiga===")
            als = int(input("Masukkan Alas :"))
            tgi = int(input("Masukkan Tinggi :"))
            luas = 1/2*als*tgi
            print("============================================")
            print("Luas segitiga dari alas", als, "tinggi", tgi, "adalah:", + (luas))
            print("============================================")
               
        elif pilihan == "2":
          print("===Keliling Segitiga===")
          s1 = float(input("Masukan sisi ke 1 dari segitiga :"))
          s2 = float(input("Masukan sisi ke 2 dari segitiga :"))
          s3 = float(input("Masukan sisi ke 3 dari segitiga :"))
          keliling = s1 + s2 + s3
          print("============================================")
          print("Keliling segitiga adalah: ", + (keliling))
          print("============================================")          
        elif pilihan == "0":
            break
        else:
            print("Maaf, Mohon Masukan Pilihan Yang Tepat")
            
def Lingkaran():
    while True:
        print("===Anda Telah Memilih Lingkaran===")
        print("1. Luas Lingkaran")
        print("2. Keliling Lingkaran")
        print("0. Keluar")
        pilihan = input("Masukan pilihan :")
        if pilihan == "1":
            print("===Luas Lingkaran===")
            phi = 3.14
            j = float(input("Masukan panjang jari-jari lingkaran :"))
            luas= phi*j*j
            print("============================================")
            print("Luas lingkaran adalah :" + str(luas))
            print("============================================")
            
        elif pilihan == "2":
          print("===Keliling Lingkaran===")
          phi = 3.14
          j = float(input("Masukan jari-jari lingkaran :"))
          keliling = 2*j*phi
          print("============================================")
          print("Keliling lingkaran adalah :" + str(keliling))
          print("============================================")          
        elif pilihan == "0":
            break
        else:
            print("Maaf, Mohon Masukan Pilihan Yang Tepat")
            
def Persegi():
    while True:
        print("===Anda Telah Memilih Persegi===")
        print("1. Luas Persegi")
        print("2. Keliling Persegi")
        print("0. keluar")
        pilihan = input("Masukan pilihan :")
        if pilihan == "1":
            print("===Luas Persegi===")
            p = float(input("Masukan panjang sisi persegi :"))
            luas= p*p
            print("============================================")
            print("Luas persegi adalah :" + str(luas))
            print("============================================")
            
        elif pilihan == "2":
          print("===Keliling Persegi===")
          p = float(input("Masukan jari-jari persegi :"))
          keliling = 4*p
          print("============================================")
          print("Keliling persegi adalah :" + str(keliling))
          print("============================================")          
        elif pilihan == "0":
            break
        else:
            print("Maaf, Mohon Masukan Pilihan Yang Tepat")
            
def Persegi_panjang():
    while True:
        print("===Anda Telah Memilih Persegi panjang===")
        print("1. Luas Persegi panjang")
        print("2. Keliling Persegi panjang")
        print("0. keluar")
        pilihan = input("Masukan pilihan :")
        if pilihan == "1":
            print("===Luas Persegi Panjang===")
            P = float(input("Masukan panjang  persegi panjang :"))
            L = float(input("Masukan lebar  persegi panjang :"))
            luas = P*L
            print("============================================")
            print("Luas persegi adalah :" + str(luas))
            print("============================================")
            
        elif pilihan == "2":
          print("===Keliling Persegi Panjang===")
          P = float(input("Masukan panjang  persegi panjang :"))
          L = float(input("Masukan lebar  persegi panjang :"))
          keliling = 2*(P+L)
          print("============================================")
          print("Keliling persegi panjang adalah :" + str(keliling))
          print("============================================")          
        elif pilihan == "0":
            break
        else:
            print("Maaf, Mohon Masukan Pilihan Yang Tepat")
                
while True:
    print("============================================")
    print("== Selamat Datang Di Program Bangun Datar ==")
    print("-------------------------------------------")
    print("Silahkan Pilih Bangun Datar:")
    print("           1.Segitiga")
    print("           2.Lingkaran")
    print("           3.Persegi")
    print("           4.Persegi Panjang")
    print("           0.keluar")
    pilihan = input("Masukan pilihan :")
    print("============================================")
    if pilihan == "1":
        Segitiga()
    elif pilihan == "2":
        Lingkaran()
    elif pilihan == "3":
        Persegi()
    elif pilihan == "4":
        Persegi_panjang()
    elif pilihan == "0":
        break
    else:
        print("Maaf, Silahkan Masukan Pilihan Yang sesuai !")