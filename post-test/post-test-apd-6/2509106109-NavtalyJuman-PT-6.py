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

print("=== SISTEM MANAJEMEN DECK CLASH ROYALE 2025 ===")

while True:
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih 1, 2, atau 3: ")

    if pilih == "1":
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            print("Selamat datang ya", username)
            if users[username]["role"] == "Admin":
                while True:
                    print("=== MENU KHUSUS ADMIN ===")
                    print("1. Lihat Semua Deck")
                    print("2. Tambah Deck")
                    print("3. Ubah Deck")
                    print("4. Hapus Deck")
                    print("5. Logout")
                    pilih_admin = input("Pilih menu: ")
                    if pilih_admin == "1":
                        if len(decks) == 0:
                            print("Belum ada deck yang ditambahkan.")
                        else:
                            for key in decks:
                                deck = decks[key]
                                print(f"ID: {key}")
                                print(f"Nama Deck: {deck['nama']}")
                                print(f"Pemain: {deck['pemain']}")
                                print(f"Strategi: {deck['strategi']}")
                                print(f"Kartu: {deck['kartu']}")

                    elif pilih_admin == "2":
                        nama = input("Nama Deck: ")
                        pemain = input("Nama Pemain: ")
                        strategi = input("Jenis Strategi: ")
                        kartu = []
                        print("Masukkan 8 kartu:")
                        for i in range(8):
                            kartu_baru = input("Kartu ke-" + str(i+1) + ": ")
                            kartu.append(kartu_baru)
                        new_id = len(decks) + 1
                        decks[new_id] = {"nama": nama, "pemain": pemain, "strategi": strategi, "kartu": kartu}
                        print("Deck berhasil ditambahkan!")

                    elif pilih_admin == "3":
                        ubah = int(input("Masukkan ID deck yang ingin diubah: "))
                        if ubah in decks:
                            nama = input("Nama Deck baru: ")
                            pemain = input("Nama Pemain baru: ")
                            strategi = input("Jenis Strategi baru: ")
                            kartu = []
                            print("Masukkan 8 kartu baru:")
                            for i in range(8):
                                kartu_baru = input("Kartu ke-" + str(i+1) + ": ")
                                kartu.append(kartu_baru)
                            decks[ubah].update({
                                "nama": nama,
                                "pemain": pemain,
                                "strategi": strategi,
                                "kartu": kartu
                            })
                            print("Deck berhasil diubah!")
                        else:
                            print("ID deck tidak ditemukan.")

                    elif pilih_admin == "4":
                        hapus = int(input("Masukkan ID deck yang ingin dihapus: "))
                        if hapus in decks:
                            konfirmasi = input("Yakin ingin menghapus? (ya/tidak): ")
                            if konfirmasi == "ya":
                                del decks[hapus]
                                print("Deck berhasil dihapus!")
                        else:
                            print("ID tidak ditemukan.")

                    elif pilih_admin == "5":
                        break
                    else:
                        print("Pilihan tidak valid!")

            else:
                while True:
                    print("=== MENU USER ===")
                    print("1. Lihat Semua Deck")
                    print("2. Logout")
                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        if len(decks) == 0:
                            print("Belum ada deck yang ditambahkan.")
                        else:
                            for key in decks:
                                deck = decks[key]
                                print(f"ID: {key}")
                                print(f"Nama Deck: {deck['nama']}")
                                print(f"Pemain: {deck['pemain']}")
                                print(f"Strategi: {deck['strategi']}")
                                print(f"Kartu: {deck['kartu']}")
                    elif pilih_user == "2":
                        break
                    else:
                        print("Pilihan tidak valid!")

        else:
            print("Login gagal! Username atau password salah.")

    elif pilih == "2":
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        if username in users:
            print("Username sudah digunakan!")
        else:
            users[username] = {"password": password, "role": "User"}
            print("Akun berhasil dibuat!")

    elif pilih == "3":
        print("Terima kasih sudah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak ada!")