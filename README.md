## Nama  : Deka Rizky Fauzan
## Nim   : 2609116052
## Kelas : B

# Sistem Manajemen Inventaris Barang
## Deskripsi Program

Program ini merupakan sistem sederhana untuk mencatat dan melihat data inventaris barang pada sebuah toko. Data barang disimpan menggunakan file JSON sehingga data yang sudah ditambahkan tetap tersimpan walaupun program ditutup dan dijalankan kembali.

Program dibuat menggunakan bahasa Python dan menggunakan perulangan while agar menu dapat digunakan terus menerus sampai pengguna memilih menu keluar.

Program memiliki beberapa fitur:

* Melihat seluruh data barang.

* Menambahkan data barang baru.

* Menyimpan data barang ke dalam file inventaris.json.

* Menjalankan menu secara terus menerus menggunakan while.

* Keluar dari program.

Penjelasan Kode
## 1. Import JSON 
<img width="140" height="26" alt="image" src="https://github.com/user-attachments/assets/2b6f3fce-7411-488c-a5ea-49eb6d4d6ca2" />

Digunakan untuk menggunakan modul JSON pada Python. Modul ini digunakan untuk membaca dan menyimpan data ke dalam file inventaris.json.

## 2. Membaca File JSON
<img width="565" height="52" alt="image" src="https://github.com/user-attachments/assets/d569c31c-10e5-44f6-ad1c-1a67889e6f78" />


Bagian ini digunakan untuk membuka file inventaris.json dan membaca data yang ada di dalamnya. Data tersebut kemudian disimpan ke dalam variabel data.

## 3. Fungsi Tambah Data
<img width="353" height="195" alt="image" src="https://github.com/user-attachments/assets/654ebf5f-5cba-4f11-8eda-4e26596328f6" />


Fungsi ini digunakan untuk menambahkan data barang baru ke dalam variabel data. Data yang dimasukkan terdiri dari nama barang, jumlah stok, dan harga barang.

## 4. Fungsi Simpan File
<img width="612" height="127" alt="image" src="https://github.com/user-attachments/assets/8c6609c9-efbe-4004-a06f-ffe0b873c225" />


Fungsi ini digunakan untuk menyimpan data yang sudah ditambahkan ke dalam file inventaris.json. Mode "w" digunakan agar data dapat ditulis dan diperbarui di dalam file.

## 5. Perulangan While
<img width="515" height="817" alt="image" src="https://github.com/user-attachments/assets/0994b739-af26-422f-b8e8-0e4d865bc693" />


Perulangan while digunakan agar program terus berjalan dan menampilkan menu sampai pengguna memilih menu keluar.

## 6. Menu Program

Program memiliki tiga pilihan menu:

Menu 1 digunakan untuk melihat data barang.
Menu 2 digunakan untuk menambahkan barang baru.
Menu 3 digunakan untuk keluar dari program.
## 7. Perulangan Menampilkan Data
<img width="372" height="125" alt="image" src="https://github.com/user-attachments/assets/10889aeb-970b-47b3-ae8f-450c923af9df" />

Bagian ini digunakan untuk menampilkan setiap data barang yang terdapat di dalam file JSON.

Penyimpanan Data

Data program disimpan dalam file:

inventaris.json

Contoh data:

"nama": "Piala FIFA Asean Cup",

"stok": "1",

"harga": "0",

Data yang sudah ditambahkan akan tetap tersimpan di file sehingga dapat dibaca kembali ketika program dijalankan.

## Bukti dan Output Program

<img width="382" height="302" alt="image" src="https://github.com/user-attachments/assets/fd3e96f6-79f7-4c5a-adb2-1e67078941ed" />


## Data Berhasil Ditambahkan

<img width="371" height="232" alt="image" src="https://github.com/user-attachments/assets/9f740bb4-7f65-4095-a221-5a142f64ab49" />

## Data Tetap Tersimpan

<img width="505" height="318" alt="image" src="https://github.com/user-attachments/assets/99fe4b65-ec0d-4953-90ae-e79ee6bda851" />

Program sistem manajemen inventaris barang berhasil dibuat menggunakan Python dan JSON. Program dapat membaca data, menambahkan data baru, menyimpan data secara permanen, serta berjalan terus menerus menggunakan while loop sampai user memilih keluar.
