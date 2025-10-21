# listNama = ["dapupu", "bambang", "ucup", "otong"]

# print(listNama[1])

# Membuat set 
# buah = {"apel", "jeruk", "mangga", "apel"}  
# print(buah)

# angka_ganjil = {1, 3, 5, 7, 9} 
# for angka in angka_ganjil:
#     print(angka)

# angka_ganjil.add(11)
# print(angka_ganjil)    

# Daftar_buku = { 
# "Buku1" : "Bumi Manusia", 
# "Buku2" : "Laut Bercerita",
# "Buku3" : "Anak Semua Bangsa"
# } 

# print(Daftar_buku["Buku2"])
# print(Daftar_buku)
# for values in Daftar_buku.items():
#     print(values)

# Biodata = { 
#     "Nama" : "Ananda Daffa Harahap", 
#     "NIM" : 2409106050, 
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"], 
#     "Mahasiswa_Aktif" : True, 
#     "Social Media" : { "Instagram" : "daffahrhap"
#      } 
# } 
# print(Biodata["Nama"])
# print(Biodata["KRS"][1])

# list_nama= dict(mahasiswa1="Daffa", mahasiswa2="Bambang",
#                  mahasiswa3="Ucup", mahasiswa4="Otong")
# print(list_nama)

# print(f"nama saya adalah {Biodata["Nama"]}") 
# print(f"Instagram : {Biodata['Social Media']['Instagram']}") 
 
# print(f"nama saya adalah {Biodata.get("Nama")}") 
# print(Biodata.get("Nama")) 

# Film = { 
# "Avenger Endgame" : "Action", 
# "Sherlock Holmes" : "Mystery", 
# "The Conjuring" : "Horror"
# } 
# #Sebelum Ditambah 
# print(Film) 
 
# Film["Zombieland"] = "Comedy" 
# Film.update({"Hours" : "Thriller"}) 
# #Setelah Ditambah 
# print(Film) 
 
# #Sebelum Ditambah 
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# 'The Conjuring': 'Horror'} 
 
# #Setelah Ditambah 
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours': 
# 'Thriller'} 

# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# } 

# print("Jumlah Data = ", len(data))
# #Sebelum Dihapus 
# print(data) 
# cache  = data.pop("Nama")

# # setelah dihapus
# print(cache)
# print(data)
# # del data["Nama"] 
 
# #Setelah diubah 
# print(data) 
 
# #memanggil data yang telah dihapus 
# print(data.get("Nama")) 
 
# {'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
 
# {'Umur': 19, 'Jurusan': 'Informatika'} 
 
# None
 
# buku = { 
#  "Buku1" : "Bumi Manusia", 
#  "Buku2" : "Laut Bercerita" 
# } 
 
# pinjam = buku.copy() 
# pinjam['Buku2'] = "Anak Semua Bangsa"
# print(pinjam)
# print(buku)

# key = "apel", "jeruk", "mangga" 
# value = 1 
# buah = dict.fromkeys(key, value) 
# print(buah)

Musik = { 
"The Chainsmoker" : ["All we Know", "The Paris"], 
"Alan Walker" : ["Alone", "Lily"], 
"Neffex" : ["Best of Me", "Memories"] 
} 
 
for penyanyi, album in Musik.items(): 
    print(f"Musik milik {penyanyi} adalah : ") 
    for song in album: 
        print(song) 
    print("")