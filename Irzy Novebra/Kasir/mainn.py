user = [{
    'username': 'kasir',
    'password': 'kasirpass'
}]

Barang = []

def DataBarang(Barang):
    nama_barang = input("Masukan Nama Barang : ")
    harga_barang = int(input("Masukan Harga Barang : "))
    jumlah_barang = int(input("Masukan Jumlah Barang : "))

    Barang.append({
        'barang': nama_barang,
        'harga': harga_barang,
        'jumlah': jumlah_barang
    })

def Pembayaran(Barang):
    total = 0
    kembali = 0

    for b in Barang:
      total += (b['harga'] *b['jumlah'])
    print("Total Harga Semua: ", total)

    uang = int(input("Uang Pembeli: "))
    kembali = uang - total
    if kembali > 0:
        print("Total Kembalian ", kembali)
        print("===================================")
        print("Indomei")
        print("===================================")
        print("Keterangan                    Harga")
        print(b['jumlah'],b['barang'],   b['harga'])
        print("===================================")
        print("Total",                        total)
        print("Bayar",                         uang)
        print("Kembali",                    kembali)
        exit()
    elif kembali < 0:
        print("Maaf uang anda kurang", kembali)
        CounterPembayaran(Barang)

def CounterPembayaran(Barang):
    while True:
        pilihan = input("Hitung lagi (y/n) : ")
        if pilihan == "y":
            Pembayaran(Barang)
        elif pilihan == "n":
            MainKasir()
        else:
            print("Pilihan Tidak Sesuai")

def MainKasir():
    while True:
        print("Menu Aplikasi : ")
        print("1. Tambah Barang ")
        print("2. Bayar Barang ")
        print("3. Logout ")

        pilihan = int(input("Pilih 1-3 : "))
        if pilihan == 1:
            DataBarang(Barang)
            MainKasir()
        elif pilihan == 2:
            if len(Barang) > 0:
                Pembayaran(Barang)
            else:
                print("Anda Belum Memasukan Produk Apa-apa")
        elif pilihan == 3:
            exit()
        else:
            print("Pilihan Tidak Sesuai")


def main():
    while True: 
       username = input('Username : ')
       password = input('Password : ')
       for u in user:
            if u['username'] == username and u['password'] == password:
                print("Login Berhasil")
                MainKasir()
            else:
                print("Terjadi Kesalahan, Silahkan input ulang")

main()
                









       


  