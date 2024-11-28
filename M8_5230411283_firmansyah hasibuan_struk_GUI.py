import tkinter as tk
from tkinter import messagebox

def tambah_item():
    nama_barang = entry_nama.get()
    jumlah = entry_jumlah.get()
    harga = entry_harga.get()

    if not (nama_barang and jumlah.isdigit() and harga.isdigit()):
        messagebox.showerror("Error", "Harap masukkan data yang valid!")
        return

    jumlah = int(jumlah)
    harga = int(harga)
    total_harga = jumlah * harga

    daftar_belanja.append({"nama": nama_barang, "jumlah": jumlah, "harga": harga})
    listbox.insert(tk.END, f"{nama_barang} - {jumlah} x {harga} = {total_harga}")

    entry_nama.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)
    entry_harga.delete(0, tk.END)

def hapus_item():
    selected_index = listbox.curselection() 
    if not selected_index:
        messagebox.showwarning("Peringatan", "Pilih item yang ingin dihapus!")
        return

    del daftar_belanja[selected_index[0]]
    listbox.delete(selected_index)

def cetak_struk():
    if not daftar_belanja:
        messagebox.showwarning("Peringatan", "Daftar belanja kosong!")
        return

    uang_dibayar = entry_uang_dibayar.get()
    if not uang_dibayar.isdigit():
        messagebox.showerror("Error", "Harap masukkan jumlah uang yang valid!")
        return

    uang_dibayar = int(uang_dibayar)
    total_harga = sum(item['jumlah'] * item['harga'] for item in daftar_belanja)
    kembalian = uang_dibayar - total_harga

    if kembalian < 0:
        messagebox.showerror("Error", "Uang yang dibayar kurang!")
        return

    struk = f"""
    {'='*30}
    {"Toko SHedulur":^30}
    {"Jl. Meranti No. 1922, Ogan Komering Ilir"}
    {'='*30}
    No  Nama Barang       Harga  Total
    {'-'*30}
    """
    for i, item in enumerate(daftar_belanja, start=1):
        struk += f"{i:<4}{item['nama']:<15}{item['jumlah']:<6}{item['harga']:<7}{item['jumlah']*item['harga']:<7}\n"

    struk += f"""
    {'-'*30}
    Total Harga: {total_harga:>17}
    Uang Dibayar: {uang_dibayar:>15}
    Kembalian: {kembalian:>18}
    {'='*30}
    """
    
    messagebox.showinfo("Struk Pembayaran", struk)

root = tk.Tk()
root.title("Struk Pembayaran")
root.configure(bg="black")

daftar_belanja = []

frame_input = tk.Frame(root, padx=10, pady=10, bg="black")
frame_input.pack()

tk.Label(frame_input, text="Nama Barang:", bg="black", fg="green").grid(row=0, column=0, sticky=tk.W)
entry_nama = tk.Entry(frame_input, width=25, bg="black", fg="green", insertbackground="green")
entry_nama.grid(row=0, column=1)

tk.Label(frame_input, text="Jumlah:", bg="black", fg="green").grid(row=1, column=0, sticky=tk.W)
entry_jumlah = tk.Entry(frame_input, width=25, bg="black", fg="green", insertbackground="green")
entry_jumlah.grid(row=1, column=1)

tk.Label(frame_input, text="Harga:", bg="black", fg="green").grid(row=2, column=0, sticky=tk.W)
entry_harga = tk.Entry(frame_input, width=25, bg="black", fg="green", insertbackground="green")
entry_harga.grid(row=2, column=1)

btn_tambah = tk.Button(frame_input, text="Tambah Item", command=tambah_item, bg="green", fg="black")
btn_tambah.grid(row=3, columnspan=2, pady=5)

frame_list = tk.Frame(root, padx=10, pady=10, bg="black")
frame_list.pack()

listbox = tk.Listbox(frame_list, width=50, height=10, bg="black", fg="green", highlightbackground="green")
listbox.pack()

btn_hapus = tk.Button(frame_list, text="Hapus Item", command=hapus_item, bg="red", fg="white")
btn_hapus.pack(pady=5)

frame_uang = tk.Frame(root, padx=10, pady=10, bg="black")
frame_uang.pack()

tk.Label(frame_uang, text="Uang Dibayar:", bg="black", fg="green").grid(row=0, column=0, sticky=tk.W)
entry_uang_dibayar = tk.Entry(frame_uang, width=25, bg="black", fg="green", insertbackground="green")
entry_uang_dibayar.grid(row=0, column=1)

btn_cetak = tk.Button(root, text="Cetak Struk", command=cetak_struk, bg="green", fg="black")
btn_cetak.pack(pady=10)

root.mainloop()
