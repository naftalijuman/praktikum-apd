User = "Navtaly Juman"
Pasword = "2509106109"

print("LOGIN APLIKASI STREAMING MUSIK")
Nama = input("Masukkan Nama Anda: ")
NIM = input("Masukkan NIM Anda: ")

if Nama == User and NIM == Pasword:
    print("Login Berhasil!")

    Biaya_Langganan = 1500000
    print("PILIHAN PAKET LANGGANAN")
    print("Harga semua paket adalah Rp 1.500.000")
    print("1. Bronze")
    print("2. Silver")
    print("3. Gold")
    print("4. Platinum")
    pilihan = input("Masukkan pilihan paket anda (1-4): ")
    
    if pilihan == "1":
        admin = 0.01
        fitur = "Akses dasar ke lagu-lagu populer"
        paket = "Bronze"
    elif pilihan == "2":
        admin = 0.03
        fitur = "Akses lagu premium dan playlist kustom"
        paket = "Silver"
    elif pilihan == "3":
        admin = 0.05
        fitur = "Akses lagu premium, playlist kustom, dan mode offline"
        paket = "Gold"
    elif pilihan == "4":
        admin = 0.07
        fitur = "Akses semua fitur, playlist kustom, mode offline, konten eksklusif artis"
        paket = "platinum"
    else:
        print("Pilihan paket tidak valid!")
        exit()

    total = Biaya_Langganan +(Biaya_Langganan * admin)
        
    print("RINCIAN PEMBAYARAN")
    print("Paket        :", paket)
    print("Fitur        :", fitur)
    print("Biaya Paket  : Rp", Biaya_Langganan)
    print("Biaya Admin  :", int(admin*100),"%")
    print("Total Bayar  : Rp", int(total))
    print("Terima kasih telah berlangganan di aplikasi streaming musik kami.")
    
else:
    print("Login gagal! Nama atau NIM salah!")
    print("Silahkan coba lagi nanti.")