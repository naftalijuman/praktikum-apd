from auth import login, register
from deck import menu_admin, menu_user

def main():
    print("\n=== SISTEM MANAJEMEN DECK CLASH ROYALE 2025 ===")
    print("===============================================")

    while True:
        print("\n1. Login")
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

if __name__ == "__main__":
    main()