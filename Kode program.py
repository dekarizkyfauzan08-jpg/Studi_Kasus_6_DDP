import json

with open("Inventaris.json", "r", encoding="utf-8") as f:
	data = json.load(f)


def tambah_data(nama, stok, harga):
	data.append({
		"nama": nama,
		"stok": stok,
		"harga": harga
	})

	return "Data ditambah"


def simpan_file():
	with open("inventaris.json", "w", encoding="utf-8") as f:
		json.dump(data, f, indent=4)

	return "Data tersimpan ke inventaris.json"


while True:
	print("\n===== SISTEM INVENTARIS BARANG =====")
	print("1. Lihat data barang")
	print("2. Tambah barang")
	print("3. Keluar")

	pilihan = input("Pilih menu: ")

	if pilihan == "1":
		print("\n===== DATA BARANG =====")

		if len(data) == 0:
			print("Belum ada data barang.")
		else:
			for barang in data:
				print("Nama:", barang["nama"])
				print("Stok:", barang["stok"])
				print("Harga:", barang["harga"])
				print()

	elif pilihan == "2":
		nama = input("Nama barang: ")
		stok = input("Jumlah stok: ")
		harga = input("Harga barang: ")

		print(tambah_data(nama, stok, harga))
		print(simpan_file())

	elif pilihan == "3":
		print("Program selesai.")
		break

	else:
		print("Pilihan tidak tersedia")
