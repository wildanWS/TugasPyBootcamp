data = [{
    'username':'k',
    'password' :'k'
}]

barang = []

def dataBarang(barang):
    Nb = input('Nama Barang:')
    Hb = int(input('Harga Barang:'))
    Bb = int(input('Banyak Barang:'))
    print('----------------------------------')
    barang.append({
        'Nama Barang': Nb,
        'Harga Barang': Hb,
        'Banyak Barang': Bb
    })
    # print(barang)
    
def counterPembayaran():
    while True:
        print('*************************')
        pilih = input('Hitung Lagi: (y/n) :')
        if pilih == 'y':
            pembayaran(barang)
            break
        elif pilih == 'n':
            mainkasir()
        else:
            print('masukan pilihan y/n')

def pembayaran(barang):
    total = 0
    i = 1
    p = 1

    for b in barang:
        print(i,'Nama : ',b['Nama Barang'], "Harga : ",b['Harga Barang'], "Jumlah : ",b['Banyak Barang'])
        i += 1
        total += b['Harga Barang'] * b['Banyak Barang']
    print('----------------------------------')
    print('Total Harga Semuanya   : ''Rp.',total)

    bayar = int(input('Masukan Uang Pembelian : ''Rp. '))
    kembalian =  bayar - total
    if bayar - total >= 0:
        print('Jumlah Kembalian : ', kembalian)
        print('*********************************************')
        print('')
        print('                 INDOINDOAN')
        print('           Alamat: Jln.Alok No.404')
        print('                 Telp.0812345')
        print('*********************************************')
        print('                STRUK PEMBAYARAN')
        print('*********************************************')
        print('NamaBarang           Harga           Jumlah')
        
        for b in barang:
            print(b['Nama Barang'],"\t\t    ",b['Harga Barang'],"\t\t",b['Banyak Barang'])
            p += 1
        print('*********************************************')
        print('Total                               Rp',total)
        print('Bayar                               Rp',bayar)
        print('Kembalian                           Rp',kembalian)
        print('*********************************************')
        print('                 Terimakasih')
        print('      Telah membeli barang di tempat kami :)')
        print()
        exit()
    else:
        print('Maap uang anda kurang  : ''Rp.',bayar - total)
        counterPembayaran()

def mainkasir():
    print('++++++++++ SELAMAT DATANG DI KASIR WARUNG KAMI ++++++++++')
    print('Menu Aplikasi : ')
    while True:
        print('1.Tambah Barang')
        print('2.Bayar Barang')
        print('3.Logout')
        pilih = int(input('Pilih 1-3 : '))
        print('----------------------------------')
        if pilih == 1:
            dataBarang(barang)
            mainkasir()
            break
        elif pilih == 2:
            if len(barang) > 0:
                pembayaran(barang)
            else:
                print('Anda Belum Memasukan Apapun')
        elif pilih == 3:
            print('Logout Berhasil...')
            main()
        else:
            print('Masukan pilihan yang tertara')
    

def main():
    while True:
        print('++++++++++ SELAMAT DATANG DI KASIR WARUNG KAMI ++++++++++')
        username = input('Username : ')
        password = input('Password : ')
        for u in data:
            if u['username'] == username and u['password'] == password:
                print('Login Berhasil')
                mainkasir()
                break
            else:
                print('Username atau password anda Salah...')

main()