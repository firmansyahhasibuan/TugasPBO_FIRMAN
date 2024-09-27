def balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return volume, luas_permukaan

panjang = 7
lebar = 4
tinggi = 3
volume_balok, luas_balok = balok(panjang, lebar, tinggi)
print(f"Volume Balok: {volume_balok}")
print(f"Luas Permukaan Balok: {luas_balok}")



def kubus(sisi):
    volume = sisi ** 3
    luas_permukaan = 6 * (sisi ** 2)
    return volume, luas_permukaan


sisi = 5
volume_kubus, luas_kubus = kubus(sisi)
print(f"Volume Kubus: {volume_kubus}")
print(f"Luas Permukaan Kubus: {luas_kubus}")
