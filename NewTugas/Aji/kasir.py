barang = []

def DataBarang(barang):
    nama = input('Masukan Nama Barang :')
    harga = int(input('Masukan Harga Barang :'))
    jumlah = int(input('Masukan Banyak Barang :'))
    print('----------------------------------')
    print('Berhasil Ditambahkan')
    print('----------------------------------')
    if len(nama) < 7:
        nama = nama + (" " * (15 - len(nama)))
    barang.append({
        'Nama Barang': nama,
        'Harga Barang': harga,
        'Banyak Barang': jumlah
    })
    
def CounterPembayaran():
    while True:
        print('*************************')
        pilih = input('Hitung Lagi: (y/n) :')
        if pilih == 'y':
            pembayaran(barang)
            break
        elif pilih == 'n':
            main_kasir()
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
    print('Total Harga Semua   : ''Rp.',total)

    bayar = int(input('Masukan Uang Pembeli : ''Rp. '))
    kembalian =  bayar - total
    if bayar - total >= 0:
        print('Jumlah Kembalian : ', kembalian)
        print('==================================================')
        print('')
        print('                 INDOINDOAN'                       )
        print('           Alamat: Jln.Alok No.2829'               )
        print('                 Telpon.0113766'                     )
        print('==================================================')
        print('                STRUK PEMBAYARAN')
        print('==================================================')
        print('Keterangan                               Harga')
        
        for b in barang:
            print(b['Banyak Barang'],b['Nama Barang'],"\t\t\t",b['Harga Barang'])
            p += 1
        print('==============================================')
        print('Total                               Rp',total)
        print('Bayar                               Rp',bayar)
        print('Kembalian                           Rp',kembalian)
        print('==============================================')
        print('                 Terimakasih')
        print('      Telah membeli barang di tempat kami ')
        print()
        exit()
    else:
        print('Maap uang anda kurang  : ''Rp.',bayar - total)
        CounterPembayaran()


def main_kasir():
    print()
    print('========SELAMAT DATANG DI PROGRAM KASIR========')
    print('Menu Aplikasi : ')
    while True:
        print('1.Tambah Barang')
        print('2.Bayar Barang')
        print('3.Logout')
        pilih = int(input('Pilih 1-3 : '))
        print('----------------------------------')
        if pilih == 1:
            DataBarang(barang)
            main_kasir()
            break
        elif pilih == 2:
            if len(barang) > 0:
                pembayaran(barang)
            else:
                print('Anda Belum Menbahkan Barang Apapun')
        elif pilih == 3:
            print('Logout Berhasil...')
            main()
        else:
            print('Masukan pilihan yang tertara')
            
            
def main():
    print('========SELAMAT DATANG DI KASIR WARUNG MAKAN========')
    username = input('masukan username kasir anda : ')
    password = input('masukan password kasir anda : ')
 
    if username == 'kasir' and password == 'kasir':
        print('login berhasil...')
        main_kasir()
        
    else:
        print('maaf, usename atau password salah..')
        main()
        
main()