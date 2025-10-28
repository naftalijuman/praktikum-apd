users = {
    "Navtaly Juman": {"password": "2509106109", "role": "Admin"}
}

decks = {
    1: {
        "nama": "Miner Control",
        "pemain": "Morten",
        "strategi": "Control",
        "kartu": ["Miner", "Poison", "Wall Breaker", "Skeletons", "Bats", "Valkyrie", "Bomb Tower", "Log"]
    },
    2: {
        "nama": "X-Bow 2.9 Cycle",
        "pemain": "Aragon",
        "strategi": "Siege",
        "kartu": ["X-Bow", "Tesla", "Ice Spirit", "Skeletons", "Ice Golem", "Fireball", "Log", "Archers"]
    },
    3: {
        "nama": "LavaLoon",
        "pemain": "Surgical Goblin",
        "strategi": "Air Beatdown",
        "kartu": ["Lava Hound", "Balloon", "Mega Minion", "Tombstone", "Minions", "Fireball", "Zap", "Miner"]
    },
    4: {
        "nama": "Royal Giant Lightning",
        "pemain": "Mohamed Light",
        "strategi": "Beatdown",
        "kartu": ["Royal Giant", "Fisherman", "Lightning", "Mother Witch", "Electro Spirit", "Skeletons", "Hunter", "Log"]
    },
    5: {
        "nama": "Bridge Spam Pekka",
        "pemain": "Ruben",
        "strategi": "Control",
        "kartu": ["Bandit", "Battle Ram", "Royal Ghost", "Dark Prince", "Magic Archer", "Pekka", "Poison", "Zap"]
    }
}

def tampilkan_deck():
    if len(decks) == 0:
        print("Belum ada deck yang ditambahkan.")
    else:
        for key, deck in decks.items():
            print(f"\nID: {key}")
            print(f"Nama Deck: {deck['nama']}")
            print(f"Pemain: {deck['pemain']}")
            print(f"Strategi: {deck['strategi']}")
            print(f"Kartu: {deck['kartu']}")

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["password"] == password:
        print(f"\nSelamat datang {username}!\n")
        return users[username]["role"], username
    else:
        print("Login gagal! Username atau password salah.")
        return None, None
def register():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    if username in users:
        print("Username sudah digunakan!")
    else:
        users[username] = {"password": password, "role": "User"}
        print("Akun berhasil dibuat!")

def tambah_deck(jumlah_kartu):
    nama = input("Nama Deck: ")
    pemain = input("Nama Pemain: ")
    strategi = input("Jenis Strategi: ")

    kartu = []
    print(f"Masukkan {jumlah_kartu} kartu:")
    for i in range(jumlah_kartu):
        kartu_baru = input(f"Kartu ke-{i+1}: ")
        kartu += [kartu_baru]
    new_id = len(decks) + 1
    decks[new_id] = {"nama": nama, "pemain": pemain, "strategi": strategi, "kartu": kartu}
    print("Deck berhasil ditambahkan!")

def hapus_deck(id_hapus):
    if id_hapus in decks:
        del decks[id_hapus]
        print("Deck berhasil dihapus!")
    else:
        print("ID deck tidak ditemukan.")

def ubah_deck(id_ubah):
    if id_ubah not in decks:
        print("ID deck tidak ditemukan.")
        return
    deck = decks[id_ubah]
    print(f"\nMengubah deck: {deck['nama']}")

    deck["nama"] = input(f"Nama baru ({deck['nama']}): ") or deck["nama"]
    deck["pemain"] = input(f"Pemain baru ({deck['pemain']}): ") or deck["pemain"]
    deck["strategi"] = input(f"Strategi baru ({deck['strategi']}): ") or deck["strategi"]

    print("Masukkan kartu baru (kosongkan jika tidak ingin mengubah):")
    kartu_baru = []
    for i in range(8):
        k = input(f"Kartu ke-{i+1} ({deck['kartu'][i]}): ")
        if k:
            kartu_baru += [k]
        else:
            kartu_baru += [deck["kartu"][i]]
    deck["kartu"] = kartu_baru
    print("Deck berhasil diubah!")

def menu_admin():
    print("\n=== MENU ADMIN ===")
    print("1. Lihat Semua Deck")
    print("2. Tambah Deck")
    print("3. Ubah Deck")
    print("4. Hapus Deck")
    print("5. Kembali ke Menu Utama")

    try:
        pilihan = int(input("Pilih menu: "))
    except ValueError:
        print("Input harus berupa angka!")
        return menu_admin()

    if pilihan == 1:
        tampilkan_deck()
    elif pilihan == 2:
        tambah_deck(8)
    elif pilihan == 3:
        try:
            id_ubah = int(input("Masukkan ID deck yang ingin diubah: "))
            ubah_deck(id_ubah)
        except ValueError:
            print("ID harus angka!")
    elif pilihan == 4:
        try:
            id_hapus = int(input("Masukkan ID deck yang ingin dihapus: "))
            hapus_deck(id_hapus)
        except ValueError:
            print("Input ID harus angka!")
    elif pilihan == 5:
        return
    else:
        print("Pilihan tidak valid!")

    menu_admin()

def menu_user():
    print("\n=== MENU USER ===")
    print("1. Lihat Semua Deck")
    print("2. Kembali ke Menu Utama")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tampilkan_deck()
        menu_user()
    elif pilihan == "2":
        print("Logout berhasil.")
    else:
        print("Pilihan tidak valid!")
        menu_user()

def main():
    print("\n=== SISTEM MANAJEMEN DECK CLASH ROYALE 2025 ===")
    print("===============================================")

    while True:
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih 1, 2, atau 3: ")

        if pilihan == "1":
            role, nama_user = login()
            if role == "Admin":
                menu_admin()
            elif role == "User":
                menu_user()
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!")
main()