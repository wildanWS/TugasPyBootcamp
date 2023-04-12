users = [
    {
        'username': 'k',
        'password': 'ks'
    }
]
Barang = []

def dataBarang(Barang):
    namaBarang = input('Masukan nama barang : ')
    hargaBarang = int(input('Masukan harga barang : '))
    jumlahBarang = int(input('Masukan jumlah barang : '))

    Barang.append({
        'barang': namaBarang,
        'harga': hargaBarang,
        'jumlah': jumlahBarang
    })

def pembayaran(Barang):
    total = 0
    kembali = 0

    for b in Barang:
        total += (b['harga'] * b['jumlah'])
    print('Total Harga Semua : Rp', total)

    uang = int(input('Uang pembelian : Rp'))
    kembali = uang - total
    if kembali > 0:
        print('Jumlah kembalian              ','Rp',kembali)
        print('======================================')
        print('                                      ')
        print('               HalalMart              ')
        print('        Alamat: Jln.Isekai No.404     ')
        print('           Telp.044444444444          ')
        print('======================================')
        print('           STRUK PEMBAYARAN           ')
        print('======================================')
        print('Keterangan                       Harga')
        for b in Barang:
         print(b['jumlah'],b['barang'],'                       ','Rp',b['harga'])
        print('======================================')
        print('Total                         ','Rp',total)
        print('Bayar                         ','Rp',uang)
        print('Kembalian                     ','Rp',kembali)
        print('======================================')
        print('             TERIMAKASIH!             ')
        print(' Telah membeli barang di tempat kami  ')
        print('                                      ')
        while True:
            print('1. Logout : ')
            print('2. Transaksi lagi : ')
            pilihan = input('Pilih 1-2 : ')
            if pilihan == '1':
              print('Logout berhasil...')
              Main()
              break
            elif pilihan == '2':
                print('Silahkan transaksi lagi...')
                menu()
            else:
               print('Pilihan tidak sesuai')
    elif kembali < 0:
        print('Maaf uang anda kurang         ','Rp',kembali)
        counterPembayaran(Barang)

def counterPembayaran(Barang):
    while True:
        pilihan = input('Hitung Lagi (y/n) : ')
        if pilihan == 'y':
            pembayaran(Barang)
        elif pilihan == 'n':
            Main()
        else:
            print('Pilihan tidak sesuai')

def menu():
    while True:
        print("== Menu Aplikasi ==")
        print('1. Tambah barang : ')
        print('2. Bayar barang : ')
        print('3. Logout : ')
        pilih = input('Pilih 1-3 : ')
        print('====================')
        if pilih == '1':
            dataBarang(Barang)
            menu()
        elif pilih == '2':
            if len(Barang) > 0:
                pembayaran(Barang)
            else:
                print('Anda belum memasukan apa-apa')
        elif pilih == '3':
            exit()
        else:
            print('Pilihan tidak sesuai')

def Main():
    while True:
        print('=====================================')
        print('==== Selamat Datang di HalalMart ====')
        print('=====================================')
        username = input('Masukan username kasir : ')
        password = input('Masukan password kasir : ')
        for u in users:
            if u['username'] == username and u['password'] == password:
                print('Logiin Berhasil...')
                menu()
            else:
                print('Maaf, username atau password anda salah...')

Main()            