# ====== Data Login ======
nama_asli = "Navtaly"
nis_asli = "12345"

# ====== Login ======
print("=== LOGIN APLIKASI STREAMING MUSIK ===")
nama = input("Masukkan Nama: ")
nis = input("Masukkan NIS: ")

# Periksa login persis
if nama == nama_asli and nis == nis_asli:
    print("\nLogin berhasil!\n")

    # ====== Menu Paket ======
    print("=== PILIHAN PAKET LANGGANAN ===")
    print("1. Bronze   - Rp 50.000")
    print("2. Silver   - Rp 100.000")
    print("3. Gold     - Rp 150.000")
    print("4. Platinum - Rp 200.000")

    pilihan = input("Pilih paket (1-4): ")

    # Hitung total dan output
    if pilihan == "1":
        harga = 50000
        admin = 0.01
        fitur = "Akses dasar ke lagu-lagu populer"
        paket = "Bronze"
    elif pilihan == "2":
        harga = 100000
        admin = 0.03
        fitur = "Akses lagu premium dan playlist kustom"
        paket = "Silver"
    elif pilihan == "3":
        harga = 150000
        admin = 0.05
        fitur = "Akses lagu premium, playlist kustom, dan mode offline"
        paket = "Gold"
    elif pilihan == "4":
        harga = 200000
        admin = 0.07
        fitur = "Semua fitur, playlist kustom, mode offline, konten eksklusif artis"
        paket = "Platinum"
    else:
        print("\nPilihan paket tidak valid!")
        exit()

    total = harga + (harga * admin)

    print("\n=== RINCIAN PEMBAYARAN ===")
    print("Paket        :", paket)
    print("Harga Paket  : Rp", harga)
    print("Biaya Admin  :", int(admin*100), "%")
    print("Total Bayar  : Rp", int(total))
    print("Keuntungan   :", fitur)
    print("\nTerima kasih telah berlangganan di aplikasi kami!")

else:
    print("\nLogin gagal! Nama atau NIS salah.")
    print("Anda tidak dapat mengakses menu pembayaran.")
