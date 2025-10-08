Username = "Navtaly Juman"
Pasword = "2509106109"

Maksimal_Login = 3
Jumlah_Login = 0
Login_Berhasil = False

print("===SELAMAT DATANG DI BIOSKOP XX0===")

while Jumlah_Login < Maksimal_Login:
    Nama = input("Masukan Username Kamu : ")
    NIM = input("Masukan Pasword Kamu : ")

    if Nama == Username and NIM == Pasword:
        print("Login Berhasil! Selamat datang,", Nama)
        Login_Berhasil = True
        break
    else:
        Jumlah_Login += 1
        Sisa_Login = Maksimal_Login - Jumlah_Login
        print("Login Salah! Jumlah Kesempatan Login Anda Tersisa :", Sisa_Login)

if not Login_Berhasil:
    print("Maaf, Anda telah mencapai batas maksimal login.")
    print("Silahkan coba lagi nanti.")
    exit()

while True:
    print("====MENU PEMBELIAN TICKET BIOSKOP XX0====")
    print("1. Ticket Reguler  - Rp 50.000")
    print("2. Ticket VIP      - Rp 100.000")
    print("3. Ticket VVIP     - Rp 150.000")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan ticket (1-4): ")

    if pilihan == "4":
        print("Terima kasih.")
        break

    if pilihan == "1":
        Ticket = "Reguler"
        Harga = 50000
    elif pilihan == "2":
        Ticket = "VIP"
        Harga = 100000
    elif pilihan == "3":
        Ticket = "VVIP"
        Harga = 150000
    else:
        print("Pilahan tidak ada! Silahakan pilih 1-4.")
        continue

    JumlahTicket = input("Masukkan Jumlah Ticket : ")
    if not JumlahTicket:
        print("Masukkan Angka Saja")
        continue
    jumlah = int(JumlahTicket)
    total = Harga * jumlah
    diskon = "Tidak ada diskon"
    potongan = 0
    if total >= 300000:
        potongan = total * 0.12
        totalAkhir = total - potongan
        diskon = "Diskon sebesar 12%"
    elif total >= 200000:
        potongan = total * 0.08
        totalAkhir = total - potongan
        diskon = "Diskon sebesar 8%"
    elif total >= 100000:
        potongan = total * 0.05
        totalAkhir = total - potongan
        diskon = "Diskon sebesar 5%"
    else:
        totalAkhir = total
        potongan = 0
        diskon = "Poster Film Ekslusif"

    print("====RINCIAN PEMBELIAN TICKET ANDA====")
    print("Jenis Ticket     :", Ticket)    
    print("Harga Ticket     : Rp", Harga)
    print("Jumlah Ticket    :", jumlah)
    print("Total Harga      : Rp", total)
    print("Potongan Harga   : Rp", int(potongan))
    print("Total Bayar      : Rp", int(totalAkhir))
    print("Anda Mendapatkan :", diskon)