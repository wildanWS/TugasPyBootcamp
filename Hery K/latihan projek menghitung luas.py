print('==============================================')
print('======Program menghitung luas & keliling======')
print('==============================================')

print('Pilih bangun datar :')
list = ['1. Segitiga', '2. Lingkaran', '3. Persegi', '4. Persegi pangjang']
for i in list:
    print(i)

pilih = input('Masukan pilihan :')
#Segitiga
if pilih == '1':
    list = ['1. Luas', '2. Keliling']
    for x in list:
        print(x)
    pilih = input('Masukan pilihan :')
    if pilih == '1':
        alas = int(input('Masukan alas segitiga :'))
        tinggi = int(input('Masukan tinggi segitiga :'))
        print('Luas dari alas segitiga', alas, 'dan tinggi segitiga',tinggi,'adalah',alas*tinggi/2)
        print('Terimakasih sudah menggunakan program saya :)')
    elif pilih == '2':
        sisi_1 = int(input('Masukan sisi a segitiga :'))
        sisi_2 = int(input('Masukan sisi b segitiga :'))
        sisi_3 = int(input('Masukan sisi c segitiga:'))
        print('Keliling dari sisi a segitiga',sisi_1,'sisi b segitiga',sisi_2,'dan sisi c segitiga',sisi_3,'adalah',sisi_1+sisi_2+sisi_3)
        print('Terimaksih sudah menggunakan program saya :)')
#Lingkaran
elif pilih == '2':
    list = ['1. Luas', '2. Keliling']
    for y in list:
        print(y)
    pilih =input('Masukan pilihan :')
    if pilih == '1':
        print('pilih \n1.jari-jari \n2.diameter')
        pilihan = input("Masukan Pilihan : ")
        if pilihan == '1':    
            jari_jari =int(input('Masukan jari-jari lingkaran :'))
            print('Luas lingkaran dari jari-jari',jari_jari,'adalah',jari_jari*2*3.14)
            print('Terimakasih sudah menggunakan program saya :)')
        elif pilihan == '2':
            diameter = int(input('Masukan Diameter lingkaran : '))
            print('Luas lingkaran dari diameter',diameter, 'adalah',(diameter/2)*3.14)
            print('Terimakasih sudah menggunakan program saya :)')
        else: 
            print('pilihan tidak sesuai')
    elif pilih == '2':
        jari_jari =int(input('Masukan jari-jari lingkaran :'))
        print('Keliling lingkaran dari jari-jari', jari_jari,'adalah',2* jari_jari*3.14)
        print('Terimaksih sudah menggunakan program saya :)')
#persegi
elif pilih == '3':
    print('1. Luas')
    print('2. Keliling')
    pilih =input('Masukan pilihan :')
    if pilih == '1':
        sisi = int(input('Masukan sisi persegi :'))
        print('Luas persegi dari sisi',sisi,'adalah', sisi**2)
        print('Terimakasih sudah menggunakan program saya :)')
    elif pilih == '2':
        sisi = int(input('Masukan sisi persegi :'))
        print('Keliling persegi dari sisi',sisi,'adalah',sisi*4)
        print('terimakasih sudah menggunakan program saya :)')
#persegi panjang
elif pilih == '4':
    print('1. Luas')
    print('2. Keliling')
    pilih = input('Masukan pilihan :')
    if pilih == '1':
        panjang = int(input('Masukan panjang :'))
        lebar = int(input('Masukan lebar :'))
        print('Luas persegi panjang dari panjang',panjang,'dan lebar',lebar,'adalah',panjang*lebar)
        print('terimakasih sudah menggunakan program saya :)')
    elif pilih == '2':
        panjang = int(input('Masukan panjang :'))
        lebar = int(input('Masukan lebar :'))
        print('Keliling persegi panjang dari panjang',panjang,'dan lebar',lebar,'adalah',2*panjang+2*lebar)
        print('terimakasih sudah menggunakan program saya :)')

else:
    print('Masukan angka yang benar ;)')
    

