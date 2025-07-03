
# fitur/pencarian.py
# Berisi fungsi pencarian berdasarkan kategori

from data.produk import daftar_produk

def cari_produk_berdasarkan_kategori(kategori):
    hasil = [p for p in daftar_produk if p["kategori"].lower() == kategori.lower()]
    return hasil

from data.produk import daftar_produk

def cari_produk_berdasarkan_kategori(kategori):
    print(f"[LOG] Mencari produk kategori: {kategori}")
    hasil = [p for p in daftar_produk if p["kategori"].lower() == kategori.lower()]
    return hasil

