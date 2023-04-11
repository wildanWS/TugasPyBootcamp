from proses import luas_segitiga, luas_persegi, luas_lingkaran, luas_persegi_panjang, keliling_lingkaran, keliling_persegi, keliling_persegi_panjang, keliling_segitiga

def segitiga():
    print()
    print("========== SEGITIGA ==========")
    print("1. Luas Segitiga")
    print("2. Keliling Segitiga")
    choice = input("Pilih: ")
    while True:
        if choice == "1":
            luas_segitiga()
            break
        elif choice == "2":
            keliling_segitiga()
            break
        else:
            choice = input("""Maaf, pilihan anda tidak tersedia!
Pilih kembali: """)



def persegi():
        print()
        print("========== PERSEGI ==========")
        print("1. Luas Persegi")
        print("2. keliling Persegi")
        choise = input("Pilih: ")
        while True:
            if choise == "1":
                luas_persegi()
                break
            elif choise == "2":
                keliling_persegi()
                break
            else:
                choise = input("""Maaf, pilihan anda tidak tersedia!
Pilih kembali: """)
    
                

def persegi_panjang():
    print()
    print("====== PERSEGI PANJANG ======")
    print("1. Luas Persegi Panjang")
    print("2. Keliling Persegi Panjang")
    choise = input("Pilih: ")
    while True: 
        if choise == "1":
            luas_persegi_panjang()
            break
        elif choise == "2":
            keliling_persegi_panjang()
            break
        else:
            choise = input("""Maaf, pilihan anda tidak tersedia!
Pilih kembali: """)


def lingkaran():
    print()
    print("======== LINGKARAN ========")
    print("1. Luas Lingkaran")
    print("2. Keliling Lingkaran")
    choise = input("Pilih: ")
    while True:
        if choise == "1":
            luas_lingkaran()
            break
        elif choise == "2":
            keliling_lingkaran()
            break
        else:
            choise = input("""Maaf, pilihan anda tidak tersedia!
Pilih kembali: """)