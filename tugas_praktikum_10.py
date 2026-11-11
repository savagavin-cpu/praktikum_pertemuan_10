# 1. tuple

#A. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama", "NIM", "Prodi").
mahasiswa = ("Muchamad Gavin Sava Willieansya", "2605060061", "Teknologi Informasi")

#B. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya.
print("NIM  :", mahasiswa[1])
print("Prodi:", mahasiswa[2])

#C. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi 
#mahasiswa[2] = "Teknologi Informasi"

#D. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali! 
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)


#2. Manipulasi Dictionary

#A. Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value 
#   berikut: - "nim": "240101" - "nama": "Budi Santoso" - "prodi": "Teknologi Informasi" 
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print(data_mahasiswa)

#B. Ubah nilai "prodi" menjadi "Sastra Mesin " sekaligus menambahkan key baru "angkatan" dengan nilai 2026. 
data_mahasiswa.update({
    "prodi": "Sastra Mesin",
    "angkatan": 2026
})
print(data_mahasiswa)

#C. Hapus data "nim", lalu tampilkan hasil akhir dictionary ke layar
del data_mahasiswa["nim"]
print(data_mahasiswa)


#3. Perulangan pada Dictionary 

#A. Buatlah dictionary bernama keranjang dengan data harga buah berikut: {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
total_belanja = 0

#B. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000" 
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")

#C. Tampilkan total belanja
total_belanja += harga
print(f"Total belanja: Rp {total_belanja}")