# main.py
# Aplikasi utama CLI untuk toko online

from data.produk import daftar_produk
from fitur.pencarian import cari_produk_berdasarkan_kategori

def tampilkan_menu():
    print("\n=== Sistem Informasi Produk Toko Online ===")
    print("1. Lihat Semua Produk")
    print("2. Cari Produk Berdasarkan Kategori")
    print("3. Keluar")

def tampilkan_produk(produk_list):
    print("\nDaftar Produk:")
    for produk in produk_list:
        print(f"- {produk['nama']} | Rp{produk['harga']} | Kategori: {produk['kategori']}")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        tampilkan_produk(daftar_produk)

    elif pilihan == "2":
        kategori = input("Masukkan kategori produk yang ingin dicari: ")
        hasil = cari_produk_berdasarkan_kategori(kategori)
        if hasil:
            tampilkan_produk(hasil)
        else:
            print("Tidak ditemukan produk pada kategori tersebut.")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
