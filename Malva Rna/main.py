from menu import segitiga, persegi, persegi_panjang, lingkaran

def main():
   
        print("    Welcome to Our Program!    ")
        print("===============================")
        print("""Pilih Bangun Datar dibawah: 
        1. Segitiga
        2. Persegi
        3. Persegi Panjang
        4. Lingkaran""")
        choise = input("Pilih: ")
        while True: 
            if choise == "1":
                segitiga()
                break
            elif choise == "2":
                persegi() 
                break
            elif choise == "3":
                persegi_panjang()
                break
            elif choise == "4":
                lingkaran()
                break
            else:
                choise = input("""Maaf, pilihan anda tidak tersedia :(
Pilih kembali: """)
                
                
            
main()