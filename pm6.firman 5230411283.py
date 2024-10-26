from typing import List
import os

class Pesanan:
    def __init__(self, nama: str, rincian: str):
        self._id: int = 0
        self.nama: str = nama
        self.rincian: str = rincian
        self.kirimans: List['Pengiriman'] = []
        
    def id(self) -> int:
        return self._id
      
    def id(self, value: int):
        self._id = value
        
    def set_pesanan(self):
        print(f"\nMemproses pesanan untuk {self.nama}")
        print(f"Rincian pesanan: {self.rincian}")
        print("Pesanan telah diproses dengan sukses!")
        
    def tambah_pengiriman(self, pengiriman: 'Pengiriman'):
        self.kirimans.append(pengiriman)
        
    def __str__(self) -> str:
        return f"Pesanan(id={self._id}, nama={self.nama}, rincian={self.rincian})"


class Pengiriman:
    def __init__(self, id: int, nama: str, informasi: str, tanggal: str, alamat: str):
        self.id: int = id
        self.nama: str = nama
        self.informasi: str = informasi
        self.tanggal: str = tanggal
        self.alamat: str = alamat
        self.status: str = "Menunggu"
        
    def proses_pengiriman(self):
        print(f"\nMemproses pengiriman untuk {self.nama}")
        print(f"Alamat pengiriman: {self.alamat}")
        print(f"Informasi pengiriman: {self.informasi}")
        print(f"Tanggal pengiriman: {self.tanggal}")
        self.status = "Sedang Diproses"
        print("Pengiriman telah diproses dengan sukses!")
        
    def __str__(self) -> str:
        return f"Pengiriman(id={self.id}, nama={self.nama}, alamat={self.alamat}, status={self.status})"


def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkan_menu():
    print("\n=== Sistem Pesanan dan Pengiriman ===")
    print("1. Buat Pesanan Baru")
    print("2. Tambah Pengiriman ke Pesanan")
    print("3. Lihat Semua Pesanan")
    print("4. Lihat Rincian Pesanan")
    print("5. Proses Pengiriman")
    print("6. Keluar")
    print("============================")


def buat_pesanan(pesanan_list: List[Pesanan]) -> Pesanan:
    print("\n=== Buat Pesanan Baru ===")
    nama = input("Masukkan nama pelanggan: ")
    rincian = input("Masukkan rincian pesanan: ")
    pesanan = Pesanan(nama=nama, rincian=rincian)
    pesanan.id = len(pesanan_list) + 1
    pesanan.set_pesanan()
    return pesanan


def tambah_pengiriman(pesanan: Pesanan) -> Pengiriman:
    print("\n=== Tambah Pengiriman Baru ===")
    pengiriman_id = len(pesanan.kirimans) + 1
    informasi = input("Masukkan informasi pengiriman: ")
    tanggal = input("Masukkan tanggal pengiriman (YYYY-MM-DD): ")
    alamat = input("Masukkan alamat pengiriman: ")
    
    pengiriman = Pengiriman(
        id=pengiriman_id,
        nama=pesanan.nama,
        informasi=informasi,
        tanggal=tanggal,
        alamat=alamat
    )
    return pengiriman


def lihat_pesanan(pesanan_list: List[Pesanan]):
    if not pesanan_list:
        print("\nTidak ada pesanan ditemukan!")
        return
    
    print("\n=== Semua Pesanan ===")
    for pesanan in pesanan_list:
        print(f"\nID Pesanan: {pesanan.id}")
        print(f"Nama Pelanggan: {pesanan.nama}")
        print(f"Rincian: {pesanan.rincian}")
        print(f"Jumlah pengiriman: {len(pesanan.kirimans)}")
        print("-" * 30)


def lihat_rincian_pesanan(pesanan_list: List[Pesanan]):
    pesanan_id = int(input("\nMasukkan ID Pesanan: "))
    pesanan = next((p for p in pesanan_list if p.id == pesanan_id), None)
    
    if pesanan is None:
        print(f"\nPesanan dengan ID {pesanan_id} tidak ditemukan!")
        return
    
    print(f"\n=== Rincian Pesanan ===")
    print(f"ID Pesanan: {pesanan.id}")
    print(f"Nama Pelanggan: {pesanan.nama}")
    print(f"Rincian: {pesanan.rincian}")
    
    if pesanan.kirimans:
        print("\nPengiriman:")
        for pengiriman in pesanan.kirimans:
            print(f"\nID Pengiriman: {pengiriman.id}")
            print(f"Status: {pengiriman.status}")
            print(f"Informasi: {pengiriman.informasi}")
            print(f"Tanggal: {pengiriman.tanggal}")
            print(f"Alamat: {pengiriman.alamat}")
    else:
        print("\nTidak ada pengiriman untuk pesanan ini.")


def proses_pengiriman(pesanan_list: List[Pesanan]):
    pesanan_id = int(input("\nMasukkan ID Pesanan: "))
    pesanan = next((p for p in pesanan_list if p.id == pesanan_id), None)
    
    if pesanan is None:
        print(f"\nPesanan dengan ID {pesanan_id} tidak ditemukan!")
        return
    
    if not pesanan.kirimans:
        print(f"\nTidak ada pengiriman ditemukan untuk ID Pesanan {pesanan_id}!")
        return
    
    print("\nPengiriman yang tersedia untuk diproses:")
    for pengiriman in pesanan.kirimans:
        print(f"ID Pengiriman: {pengiriman.id}, Status: {pengiriman.status}")
    
    pengiriman_id = int(input("\nMasukkan ID Pengiriman yang akan diproses: "))
    pengiriman = next((p for p in pesanan.kirimans if p.id == pengiriman_id), None)
    
    if pengiriman is None:
        print(f"\nPengiriman dengan ID {pengiriman_id} tidak ditemukan!")
        return
    
    pengiriman.proses_pengiriman()


# Program Utama
pesanan_list: List[Pesanan] = []

def main():
    while True:
        bersihkan_layar()
        tampilkan_menu()
        
        pilihan = input("\nMasukkan pilihan Anda (1-6): ")
        
        if pilihan == '1':
            pesanan = buat_pesanan(pesanan_list)
            pesanan_list.append(pesanan)
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '2':
            if not pesanan_list:
                print("\nTidak ada pesanan tersedia! Silakan buat pesanan terlebih dahulu.")
                input("\nTekan Enter untuk melanjutkan...")
                continue
                
            print("\nPesanan yang Tersedia:")
            for pesanan in pesanan_list:
                print(f"ID Pesanan: {pesanan.id}, Pelanggan: {pesanan.nama}")
            
            pesanan_id = int(input("\nMasukkan ID Pesanan untuk menambah pengiriman: "))
            pesanan = next((p for p in pesanan_list if p.id == pesanan_id), None)
            
            if pesanan:
                pengiriman = tambah_pengiriman(pesanan)
                pesanan.tambah_pengiriman(pengiriman)
                print("\nPengiriman berhasil ditambahkan!")
            else:
                print(f"\nPesanan dengan ID {pesanan_id} tidak ditemukan!")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '3':
            lihat_pesanan(pesanan_list)
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '4':
            lihat_rincian_pesanan(pesanan_list)
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '5':
            proses_pengiriman(pesanan_list)
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '6':
            print("\nTerima kasih telah menggunakan Sistem Pesanan dan Pengiriman!")
            break
            
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")
            input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()
