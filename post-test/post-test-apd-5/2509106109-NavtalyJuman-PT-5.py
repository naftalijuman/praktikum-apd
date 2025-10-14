import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

user = [["Navtaly Juman", "2509106109", "Admin"]]   

deck = [
    ["Miner Control", "Morten", "Control", 
     ["Miner", "Poison", "Wall Breaker","Skeletons", "Bats", "Valkyrie", "Bomb Tower","Log"]],
    ["X-Bow 2.9 Cycle", "Aragon", "Siege",
     ["X-Bow", "Tesla", "Ice Spirit","Skeletons", "Ice Golem", "Fireball","Log", "Archers"]],
    ["LavaLoon", "Surgical Goblin", "Air Beatdown",
     ["Lava Hound", "Balloon", "Mega Minion","Tombstone", "Minions", "Fireball","Zap", "Miner"]],
    ["Royale Giant", "Mohamed Light", "Beatdown",
     ["Royal Giant", "Fisherman", "Lightning","Mother Witch", "Electro Spirit","Skeletons", "Hunter", "Log"]],  
    ["Bridge Spam", "Ruben", "Control",
     ["Bandit", "Battle Ram", "Royale Ghost","Dark Prince", "Magic Archer", "Pekka","Poison", "Zap"]]
]

def tampil_deck():
    clear()
    print("===DAFTAR DECK TEMPUR CLASH ROYALE 2025===")
    if not deck:
        print("Belum ada deck yang ditambahkan.")
    else:
        for i, d in enumerate(deck):
            print(f"\n{i+1}. {d[0]} - {d[1]} ({d[2]})")
            print("   Kartu:", end=" ")
            for kartu in d[3]:
                print(kartu, end=", ")
        print()
    input("\nTekan Enter untuk kembali...")

def tambah_deck():
    clear()
    print("===TAMBAH DECK TEMPUR CLASH ROYALE 2025===")
    nama = input("Nama Deck: ")
    pemain = input("Nama Pemain: ")
    strategi = input("Jenis Strategi: ")
    kartu = []
    for i in range(8):
        kartu.append(input(f"Masukkan Kartu ke-{i+1}: "))
    deck.append([nama, pemain, strategi, kartu])
    print("\nDeck berhasil ditambahkan!")
    input("Tekan Enter untuk kembali...")

def ubah_deck():
    clear()
    print("===UBAH DECK TEMPUR CLASH ROYALE 2025===")
    tampil_deck()
    indeks = int(input("\nPilih nomor deck yang ingin diubah: ")) - 1  
    if 0 <= indeks < len(deck):
        nama = input("Nama deck baru: ")
        pemain = input("Nama pemain baru: ")
        strategi = input("Jenis strategi baru: ")
        kartu_baru = []
        for i in range(8):
            kartu_baru.append(input(f"Masukkan Kartu ke-{i+1}: "))
        deck[indeks] = [nama, pemain, strategi, kartu_baru]
        print("\nDeck berhasil diubah!")
    else:
        print("Nomor deck tidak valid.")
    input("Tekan Enter untuk kembali...")

def hapus_deck():
    clear()
    print("===HAPUS DECK TEMPUR CLASH ROYALE 2025===")
    tampil_deck()
    indeks = int(input("\nPilih nomor deck yang ingin dihapus: ")) - 1  
    if 0 <= indeks < len(deck):
        konfirmasi = input("Apakah Anda yakin ingin menghapus deck ini? (ya/tidak): ")
        if konfirmasi == "ya":
            del deck[indeks]
            print("\nDeck berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Nomor deck tidak valid.")
    input("Tekan Enter untuk kembali...")

def menu_admin():
    while True:
        clear()
        print("===MENU ADMIN CLASH ROYALE 2025===")
        print("1. Lihat Semua Deck")
        print("2. Tambah Deck")
        print("3. Ubah Deck")
        print("4. Hapus Deck")
        print("5. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampil_deck()
        elif pilihan == '2':
            tambah_deck()
        elif pilihan == '3':
            ubah_deck()
        elif pilihan == '4':
            hapus_deck()
        elif pilihan == '5':
            break
        else:
            input("Pilihan tidak valid! Tekan Enter untuk coba lagi...")

def menu_user():
    while True:
        clear()
        print("===MENU USER CLASH ROYALE 2025===")
        print("1. Lihat Semua Deck")
        print("2. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampil_deck()
        elif pilihan == '2':
            break
        else:
            input("Pilihan tidak valid! Tekan Enter untuk coba lagi...")

def register():
    clear()
    print("===REGISTER USER BARU===")
    username = input("Username baru: ")
    password = input("Pasword baru: ")
    user.append([username, password, "User"])
    print("\nAkun berhasil dibuat! Silakan login.")
    input("Tekan Enter...")           

def login():
    clear()
    print("===LOGIN CLASH ROYALE 2025===")
    username = input("Username: ")
    password = input("Password: ")

    for u in user:
        if u[0] == username and u[1] == password:
            print(f"\nSelamat datang, {username}!\n")
            input("Tekan Enter untuk masuk...")
            if u[2] == "Admin":
                menu_admin()
            else:
                menu_user()
            return
        print("Login gagal! Username atau password salah.")   
        input("Tekan Enter...")     

while True:
    clear()
    print("===SISTEM MANAJEMEN DECK CLASH ROYALE 2025===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        login()
    elif pilihan == '2':
        register()
    elif pilihan == '3':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        input("Pilihan tidak valid! Tekan Enter...")