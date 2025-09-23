# Input data
nama = input("Masukkan nama lengkap anda: ")
nim = input("Masukkan NIM anda: ")
harga = float(input("Masukkan harga laptop: Rp "))

# Daftar diskon dalam persen
laptop = {"Acer": 5, "Asus": 7, "Lenovo": 10}

# Output awal
print("===================================")
print(f"{nama} dengan NIM {nim} ingin membeli laptop seharga Rp {harga:,.0f}")
print("Berikut harga laptop setelah diskon tiap merek:")
print("===================================")

# Header tabel 
print("Merek\t Diskon\t Harga Akhir")
print("-----------------------------------")

# Isi tabel
for merek, diskon_persen in laptop.items():
    diskon = harga * (diskon_persen / 100)
    harga_akhir = harga - diskon
    print(f"{merek}\t   {diskon_persen}%\tRp{harga_akhir:,.0f}")
print("-----------------------------------") 