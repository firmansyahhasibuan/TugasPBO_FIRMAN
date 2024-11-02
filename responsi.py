from typing import List
import os

class Item:
    def __str__(self):
        return "Item"

class Makanan(Item):
    _id_counter = 1

    def __init__(self, nama: str, harga: float):
        self._id = Makanan._id_counter
        Makanan._id_counter += 1
        self.nama = nama
        self.harga = harga

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f"{self.nama} - Rp{self.harga:.2f}"

class Pesanan(Item):
    _id_counter = 1

    def __init__(self, nama_pelanggan: str):
        self._id = Pesanan._id_counter
        Pesanan._id_counter += 1
        self.nama_pelanggan = nama_pelanggan
        self.makanan: List[Makanan] = []

    @property
    def id(self):
        return self._id

    def tambah_makanan(self, makanan: Makanan):
        self.makanan.append(makanan)

    def total_harga(self):
        return sum(m.harga for m in self.makanan)

    def tampilkan_struk(self):
        print("\n=== STRUK PEMBELIAN ===")
        print(f"Pesanan ID: {self.id}")
        print(f"Nama Pelanggan: {self.nama_pelanggan}")
        print("Makanan:")
        for m in self.makanan:
            print(f"- {m}")
        print(f"Total: Rp{self.total_harga():.2f}")
        print("========================")

    def __str__(self):
        makanan_list = ', '.join(str(m) for m in self.makanan)
        return f"Pesanan ID: {self.id}, Pelanggan: {self.nama_pelanggan}, Makanan: [{makanan_list}], Total: Rp{self.total_harga():.2f}"

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    print("\n=== Sistem Pesanan Makanan ===")
    print("1. Tambah Makanan")
    print("2. Buat Pesanan Baru")
    print("3. Lihat Semua Pesanan")
    print("4. Lihat Rincian Pesanan")
    print("5. Tampilkan Struk Pembelian")
    print("6. Keluar")
    print("============================")

def tambah_makanan(makanan_list: List[Makanan]):
    nama = input("Masukkan nama makanan: ")
    while True:
        try:
            harga = float(input("Masukkan harga makanan: "))
            if harga < 0:
                print("Harga tidak boleh negatif. Silakan masukkan harga yang valid.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka untuk harga.")
    
    makanan = Makanan(nama, harga)
    makanan_list.append(makanan)
    print(f"Makanan '{nama}' berhasil ditambahkan!")

def buat_pesanan(makanan_list: List[Makanan]) -> Pesanan:
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    pesanan = Pesanan(nama_pelanggan)

    print("\nMakanan yang tersedia:")
    for makanan in makanan_list:
        print(f"{makanan.id}. {makanan}")

    while True:
        try:
            makanan_id = int(input("Masukkan ID makanan untuk ditambahkan (0 untuk selesai): "))
            if makanan_id == 0:
                break
            makanan = next((m for m in makanan_list if m.id == makanan_id), None)
            if makanan:
                pesanan.tambah_makanan(makanan)
                print(f"{makanan.nama} ditambahkan ke pesanan.")
            else:
                print("Makanan tidak ditemukan!")
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")

    return pesanan

def lihat_pesanan(pesanan_list: List[Pesanan]):
    if not pesanan_list:
        print("\nTidak ada pesanan ditemukan!")
        return
    for pesanan in pesanan_list:
        print(pesanan)

def lihat_rincian_pesanan(pesanan_list: List[Pesanan]):
    try:
        pesanan_id = int(input("Masukkan ID Pesanan: "))
        pesanan = next((p for p in pesanan_list if p.id == pesanan_id), None)
        if pesanan:
            print(pesanan)
        else:
            print("Pesanan tidak ditemukan!")
    except ValueError:
        print("Input tidak valid!")

def main():
    makanan_list: List[Makanan] = []
    pesanan_list: List[Pesanan] = []

    while True:
        bersihkan_layar()
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == '1':
            tambah_makanan(makanan_list)
        elif pilihan == '2':
            if not makanan_list:
                print("Tidak ada makanan tersedia! Silakan tambahkan makanan terlebih dahulu.")
            else:
                pesanan = buat_pesanan(makanan_list)
                pesanan_list.append(pesanan)
        elif pilihan == '3':
            lihat_pesanan(pesanan_list)
        elif pilihan == '4':
            lihat_rincian_pesanan(pesanan_list)
        elif pilihan == '5':
            if not pesanan_list:
                print("Tidak ada pesanan untuk ditampilkan!")
            else:
                pesanan_id = int(input("Masukkan ID Pesanan untuk ditampilkan struk: "))
                pesanan = next((p for p in pesanan_list if p.id == pesanan_id), None)
                if pesanan:
                    pesanan.tampilkan_struk()
                else:
                    print("Pesanan tidak ditemukan!")
        elif pilihan == '6':
            print("Terima kasih telah menggunakan sistem!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
