class Debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.nama = nama
        self.ktp = ktp
        self.limit_pinjaman = limit_pinjaman

class Manajemen:
    def __init__(self):
        self.debitur_list = []
        self.pinjaman_list = []

    def tambah_debitur(self, nama, ktp, limit_pinjaman):
        if any(d.ktp == ktp for d in self.debitur_list):
            print("KTP sudah terdaftar.")
            return
        self.debitur_list.append(Debitur(nama, ktp, limit_pinjaman))
        print(f"Debitur {nama} berhasil ditambahkan.")

    def tampilkan_debitur(self):
        for d in self.debitur_list:
            print(f"{d.nama} - Limit: {d.limit_pinjaman}")

    def tambah_pinjaman(self, nama, jumlah, bunga, durasi):
        debitur = next((d for d in self.debitur_list if d.nama.lower() == nama.lower()), None)
        if not debitur:
            print("Debitur tidak ditemukan.")
            return
        if jumlah > debitur.limit_pinjaman:
            print("Jumlah pinjaman melebihi limit.")
            return
        cicilan = jumlah * (bunga/12) / (1 - (1 + bunga/12) ** -durasi)
        self.pinjaman_list.append((nama, jumlah, bunga, durasi, cicilan))
        print(f"Pinjaman untuk {nama} berhasil ditambahkan.")

    def tampilkan_pinjaman(self, nama):
        for p in self.pinjaman_list:
            if p[0].lower() == nama.lower():
                print(f"Pinjaman: {p[1]}, Bunga: {p[2]}, Durasi: {p[3]} bulan, Cicilan: {p[4]:.2f}")

def main():
    manajemen = Manajemen()
    while True:
        print("\n1. Tambah Debitur\n2. Tampilkan Debitur\n3. Tambah Pinjaman\n4. Tampilkan Pinjaman\n5. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            nama = input("Nama: ")
            ktp = input("KTP: ")
            limit = float(input("Limit Pinjaman: "))
            manajemen.tambah_debitur(nama, ktp, limit)
        elif pilihan == "2":
            manajemen.tampilkan_debitur()
        elif pilihan == "3":
            nama = input("Nama Debitur: ")
            jumlah = float(input("Jumlah Pinjaman: "))
            bunga = float(input("Bunga (misal 0.05 untuk 5%): "))
            durasi = int(input("Durasi (bulan): "))
            manajemen.tambah_pinjaman(nama, jumlah, bunga, durasi)
        elif pilihan == "4":
            nama = input("Nama Debitur: ")
            manajemen.tampilkan_pinjaman(nama)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
