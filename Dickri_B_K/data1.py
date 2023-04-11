from dataa import luasSegitiga, kelilingSegitiga, luasLingkaran, kelilingLingkaran, luasPersegi, kelilingPersegi, luasPersegiPanjang, kelilingPersegiPanjang

def segitiga():
    print("pilih salah satu : ")
    print("                 1. Luas segitiga")
    print("                 2. Keliling segitiga")
    pilih = input('Masukan pilihan : ')
    if pilih == '1':
        luasSegitiga()
    elif pilih == '2':
        kelilingSegitiga()

def lingkaran():
    print("pilih salah satu : ")
    print("                 1. Luas lingkaran")
    print("                 2. Keliling lingkaran")
    pilih = input('Masukan pilihan : ')
    if pilih == '1':
        luasLingkaran()
    elif pilih == '2':
        kelilingLingkaran()

def persegi():
    print("pilih salah satu : ")
    print("                 1. Luas persegi")
    print("                 2. Keliling persegi")
    pilih = input('Masukan pilihan : ')
    if pilih == '1':
        luasPersegi()
    elif pilih == '2':
        kelilingPersegi()

def persegiPanjang():
    print("pilih salah satu : ")
    print("                 1. Luas persegiPanjang")
    print("                 2. Keliling persegiPanjang")
    pilih = input('Masukan pilihan : ')
    if pilih == '1':
        luasPersegiPanjang()
    elif pilih == '2':
        kelilingPersegiPanjang()