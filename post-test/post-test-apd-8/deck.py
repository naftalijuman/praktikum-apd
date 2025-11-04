from prettytable import PrettyTable

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

from prettytable import PrettyTable

def tampilkan_deck():
    if not decks:
        print("Belum ada deck yang ditambahkan.")
        return

    table = PrettyTable(["ID", "Nama Deck", "Pemain", "Strategi", "Kartu"])
    for key, deck in decks.items():
        table.add_row([key, deck["nama"], deck["pemain"], deck["strategi"], ", ".join(deck["kartu"])])
    table.align = "l"
    table.max_width = 50
    print(table)

def tambah_deck(jumlah_kartu):
    nama = input("Nama Deck: ")
    pemain = input("Nama Pemain: ")
    strategi = input("Jenis Strategi: ")

    kartu = []
    print(f"Masukkan {jumlah_kartu} kartu:")
    for i in range(jumlah_kartu):
        kartu.append(input(f"Kartu ke-{i+1}: "))

    new_id = len(decks) + 1
    decks[new_id] = {"nama": nama, "pemain": pemain, "strategi": strategi, "kartu": kartu}
    print("Deck berhasil ditambahkan!")

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
        kartu_baru.append(k if k else deck["kartu"][i])
    deck["kartu"] = kartu_baru
    print("Deck berhasil diubah!")

def hapus_deck(id_hapus):
    if id_hapus in decks:
        del decks[id_hapus]
        print("Deck berhasil dihapus!")
    else:
        print("ID deck tidak ditemukan.")

def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat Semua Deck")
        print("2. Tambah Deck")
        print("3. Ubah Deck")
        print("4. Hapus Deck")
        print("5. Kembali ke Menu Utama")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_deck()
        elif pilihan == "2":
            tambah_deck(8)
        elif pilihan == "3":
            try:
                id_ubah = int(input("Masukkan ID deck yang ingin diubah: "))
                ubah_deck(id_ubah)
            except ValueError:
                print("ID harus berupa angka!")
        elif pilihan == "4":
            try:
                id_hapus = int(input("Masukkan ID deck yang ingin dihapus: "))
                hapus_deck(id_hapus)
            except ValueError:
                print("ID harus berupa angka!")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")

def menu_user():
    while True:
        print("\n=== MENU USER ===")
        print("1. Lihat Semua Deck")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_deck()
        elif pilihan == "2":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid!")