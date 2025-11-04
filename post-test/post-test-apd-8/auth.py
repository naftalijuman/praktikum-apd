# auth.py
users = {
    "Navtaly Juman": {"password": "2509106109", "role": "Admin"}
}

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