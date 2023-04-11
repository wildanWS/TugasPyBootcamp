data = [{
    'username' : 'kasir',
    'password' : 'kasirpass'
}]

barang = []

def dataBarang(barang):
    Nb = input('Nama Barang :')
    Hb = int(input('Harga Barang :'))
    Bb = int(input('Banyak Barang :'))
    print(40*'-')
    barang.append({
        'Nama Barang': Nb,
        'Harga Barang': Hb,
        'Banyak Barang': Bb
    })
    print('\tBarang Masuk Ke Keranjang')

def counterPembayaran():
    while True:
        print(40*'-')
        try:
            pilih = input('hitung lagi?y/n : ')
            print(40*'-')
            if pilih == 'y':
                pembayaran(barang)
                break
            elif pilih == 'n':
                mainkasir()
            else:
                print('masukan pilihan y/n')
        except ValueError:
            print('Hanya Bisa Menginputkan Angka')

def pembayaran(barang):
    total = 0
    i = 1
    p = 1

    for b in barang:
        print(i,"Name :", b['Nama Barang'], "Harga : ", b['Harga Barang'],"Jumlah : ", b['Banyak Barang'])
        i += 1
        total +=  b['Harga Barang'] * b['Banyak Barang']
    print('Total Harga Semuanya : ',total)
    print(40*'-')

    bayar = int(input('Masukan Uang Pembeli : '))
    kembalian = bayar - total
    if bayar - total >= 0:
        print('Jumlah Kembalian : ',kembalian)
        print(40*'-')
        print('\t      IndoIndoan')
        print('\tAlamat : Freedom World')
        print('\t  Telp : 088328233864')
        print(40*'-')
        print(12*'-','STRUK PEMBELIAN',11*'-')
        print(40*'-')
        print('Nama Barang  ||  Harga  ||  Jumlah')
        # print(b['Banyak Barang'], b['Nama Barang'],total)
        # k += 1
        for b in barang:
            print(b['Nama Barang'],"\t\t",b['Harga Barang'],"\t   ",b['Banyak Barang'])
            p += 1
        print(40*'-')
        print('Total                      ',total)
        print('Bayar                      ',bayar)
        print('Kembalian                  ',kembalian)
        print(40*'-')
        print('Terimakasih')
        exit()
    else:
        print(40*'-')
        print('maaf uang anda kurang : ',bayar - total)
        counterPembayaran()
            
def mainkasir():
    while True:
        print(40*'-')
        print('1.Tambah Barang')
        print('2.Bayar Barang')
        print('3.Logout')
        try:
            pilih = int(input('Pilih 1-3 : '))
            print(40*'-')
            if pilih == 1:
                dataBarang(barang)
                mainkasir()
                break
            elif pilih == 2:
                if len(barang) > 0:
                    pembayaran(barang)
                else:
                    print('Anda belum memasukan apapun')
            elif pilih == 3:
                print('Logout Berhasil')
                main()
            else:
                print('Masukan Pilihan yang Tertera')
        except ValueError:
            print('Hanya Bisa Menginputkan Angka')

def main():
    while True:
        print(40*'-','Login',40*'-')
        username = input('Username : ')
        password = input('Password : ')
        for u in data:
            if u['username'] == username and u['password'] == password:
                print('Login Berhasil')
                mainkasir()
                break
            else:
                print("Username Atau Password Salah")
main()