import os
import datetime
from database import inisialisasi, baca_tiket, simpan_tiket, baca_pesan, simpan_pesan, id_baru, reset_data
from struktur_data import LinkedListQueue, HashMap
from algoritma import bubble_sort, binary_search

antrian = LinkedListQueue()


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def jeda():
    input("\n  [Enter] kembali...")

def rp(n):
    return f"Rp {int(float(n)):,}".replace(",", ".")

def cari_baris(data, key, nilai):
    for baris in data:
        if baris[key] == nilai:
            return baris
    return None

# ========== CRUD ==========
# ── TIKET ──────────────────────────────────────────

def tambah_tiket():  #menambahkan tiket
    clear()
    print("=== TAMBAH TIKET ===\n")
    semua = baca_tiket()
    id_t  = id_baru("0", semua)
    print(f"  ID baru: {id_t}")
    event  = input("  Event    : ").strip()
    tgl    = input("  Tanggal  : ").strip()
    lokasi = input("  Lokasi   : ").strip()
    try:
        harga = int(input("  Harga    : ").strip())
        kuota = int(input("  Kuota    : ").strip())
    except ValueError:
        print("  Harga/kuota harus angka."); jeda(); return

    tiket = {"id": id_t, "event": event, "tanggal": tgl, "lokasi": lokasi,
             "harga": str(harga), "kuota": str(kuota), "tersedia": str(kuota)}
    semua.append(tiket)
    simpan_tiket(semua)
    print(f"\n  Tiket {id_t} berhasil ditambahkan.")
    jeda()


def lihat_tiket():  # melihat tiket di list
    clear()
    print("=== DAFTAR TIKET ===\n")
    print("  Urutkan: 1=Nama  2=Harga naik  3=Harga turun  4=Tanggal  [Enter]=default")
    p    = input("  Pilih: ").strip()
    data = baca_tiket()
    if p == "1":   data = bubble_sort(data, "event")
    elif p == "2": data = bubble_sort(data, "harga")
    elif p == "3": data = bubble_sort(data, "harga", terbalik=True)
    elif p == "4": data = bubble_sort(data, "tanggal")

    print(f"\n  {'ID':<6} {'EVENT':<22} {'TANGGAL':<12} {'LOKASI':<10} {'HARGA':>10} {'SISA':>5}")
    print("  " + "-"*65)
    for t in data:
        print(f"  {t['id']:<6} {t['event']:<22} {t['tanggal']:<12} {t['lokasi']:<10} {rp(t['harga']):>10} {t['tersedia']:>5}")
    jeda()


def update_tiket():  # Mengubah tiket yang ada di list
    clear()
    print("=== UPDATE TIKET ===\n")
    semua = baca_tiket()
    for t in semua:
        print(f"  {t['id']}  {t['event']}")
    print()
    id_t = input("  ID tiket: ").strip().upper()
    t = cari_baris(semua, "id", id_t)
    if not t:
        print("  Tidak ditemukan."); jeda(); return

    print("  (Enter = tidak diubah)\n")
    event  = input(f"  Event   [{t['event']}]: ").strip()   or t['event']
    tgl    = input(f"  Tanggal [{t['tanggal']}]: ").strip() or t['tanggal']
    lokasi = input(f"  Lokasi  [{t['lokasi']}]: ").strip()  or t['lokasi']
    h      = input(f"  Harga   [{t['harga']}]: ").strip()   or t['harga']
    k      = input(f"  Kuota   [{t['kuota']}]: ").strip()   or t['kuota']

    terjual  = int(t['kuota']) - int(t['tersedia'])
    tersedia = max(0, int(k) - terjual)
    baru = {"id": id_t, "event": event, "tanggal": tgl, "lokasi": lokasi,
            "harga": h, "kuota": k, "tersedia": str(tersedia)}

    simpan_tiket([baru if x["id"] == id_t else x for x in semua])
    print("  Tiket diperbarui.")
    jeda()


def hapus_tiket():  # Menghapus tiket yang ada di list
    clear()
    print("=== HAPUS TIKET ===\n")
    semua = baca_tiket()
    for t in semua:
        print(f"  {t['id']}  {t['event']}")
    print()
    id_t = input("  ID tiket: ").strip().upper()
    if not cari_baris(semua, "id", id_t):
        print("  Tidak ditemukan."); jeda(); return

    aktif = any(p["id_tiket"] == id_t and p["status"] == "Aktif" for p in baca_pesan())
    if aktif:
        print("  Masih ada pemesanan aktif, tidak bisa dihapus."); jeda(); return

    if input(f"  Hapus {id_t}? (y/n): ").lower() != "y":
        return
    simpan_tiket([t for t in semua if t["id"] != id_t])
    print("  Tiket dihapus.")
    jeda()


def cari_tiket():  # Pencari tiket
    clear()
    print("=== CARI TIKET ===\n")
    print("  1=Nama event   2=Lokasi   3=ID (HashMap)")
    pilih = input("  Pilih: ").strip()
    kata  = input("  Kata kunci: ").strip()
    data  = baca_tiket()

    if pilih == "3":
        hm = HashMap()
        for t in data:
            hm.set(t["id"], t)
        hasil = [hm.get(kata.upper())] if hm.get(kata.upper()) else []
    else:
        key     = "event" if pilih == "1" else "lokasi"
        terurut = bubble_sort(data, key)
        idx     = binary_search(terurut, key, kata)
        hasil   = [r for r in data if kata.lower() in r[key].lower()] if idx >= 0 else []

    if hasil:
        print(f"\n  Ditemukan {len(hasil)} tiket:")
        for t in hasil:
            print(f"  {t['id']}  {t['event']}  {t['lokasi']}  {rp(t['harga'])}")
    else:
        print("  Tidak ditemukan.")
    jeda()


# ── PEMESANAN ──────────────────────────────────────

def buat_pemesanan():  # Membuat Pemesanan Tiket yang sudah di dalam list
    clear()
    print("=== BUAT PEMESANAN ===\n")
    tikets = baca_tiket()
    for t in tikets:
        if int(t["tersedia"]) > 0:
            print(f"  {t['id']}  {t['event']}  {rp(t['harga'])}  sisa: {t['tersedia']}")
    print()
    id_t  = input("  Pilih ID tiket: ").strip().upper()
    tiket = cari_baris(tikets, "id", id_t)
    if not tiket or int(tiket["tersedia"]) <= 0:
        print("  Tiket tidak tersedia."); jeda(); return

    nama  = input("  Nama pemesan: ").strip()
    email = input("  Email       : ").strip()
    try:
        jml = int(input("  Jumlah tiket: ").strip())
        if jml <= 0 or jml > int(tiket["tersedia"]):
            raise ValueError
    except ValueError:
        print(f"  Jumlah tidak valid (maks {tiket['tersedia']})."); jeda(); return

    total   = jml * int(float(tiket["harga"]))
    semua_p = baca_pesan()
    id_p    = id_baru("P", semua_p)

    pesan = {"id": id_p, "id_tiket": id_t, "pemesan": nama, "email": email,
             "jumlah": str(jml), "total": str(total),
             "waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
             "status": "Aktif"}

    antrian.enqueue(pesan)
    data_pesan = antrian.dequeue()

    semua_p.append(data_pesan)
    simpan_pesan(semua_p)

    for t in tikets:
        if t["id"] == id_t:
            t["tersedia"] = str(int(t["tersedia"]) - jml)
    simpan_tiket(tikets)

    print(f"\n  Pemesanan berhasil! ID: {id_p}")
    print(f"  {nama}  x{jml} tiket  Total: {rp(total)}")
    jeda()


def lihat_pemesanan():  # Melihat Pemesanan di list
    clear()
    print("=== DAFTAR PEMESANAN ===\n")
    print("  Filter: 1=Semua  2=Aktif  3=Dibatalkan")
    p    = input("  Pilih: ").strip()
    data = baca_pesan()
    if p == "2":   data = [x for x in data if x["status"] == "Aktif"]
    elif p == "3": data = [x for x in data if x["status"] == "Dibatalkan"]
    data = bubble_sort(data, "waktu", terbalik=True)

    print(f"\n  {'ID':<6} {'PEMESAN':<18} {'TIKET':<6} {'JML':>4} {'TOTAL':>12} {'STATUS'}")
    print("  " + "-"*58)
    for x in data:
        print(f"  {x['id']:<6} {x['pemesan']:<18} {x['id_tiket']:<6} {x['jumlah']:>4} {rp(x['total']):>12} {x['status']}")
    jeda()


def update_pemesanan():  # Mengubah Pemesanan yang ada di list
    clear()
    print("=== UPDATE PEMESANAN ===\n")
    id_p  = input("  ID pemesanan: ").strip().upper()
    semua = baca_pesan()
    p     = cari_baris(semua, "id", id_p)
    if not p:
        print("  Tidak ditemukan."); jeda(); return

    nama  = input(f"  Nama  [{p['pemesan']}]: ").strip() or p['pemesan']
    email = input(f"  Email [{p['email']}]: ").strip()   or p['email']

    for x in semua:
        if x["id"] == id_p:
            x["pemesan"] = nama
            x["email"]   = email
    simpan_pesan(semua)
    print("  Data diperbarui.")
    jeda()


def batalkan_pemesanan():  # Membatalkan Pemesanan
    clear()
    print("=== BATALKAN PEMESANAN ===\n")
    id_p  = input("  ID pemesanan: ").strip().upper()
    semua = baca_pesan()
    p     = cari_baris(semua, "id", id_p)
    if not p:
        print("  Tidak ditemukan."); jeda(); return
    if p["status"] == "Dibatalkan":
        print("  Sudah dibatalkan sebelumnya."); jeda(); return
    if input(f"  Batalkan {id_p} atas nama {p['pemesan']}? (y/n): ").lower() != "y":
        return

    for x in semua:
        if x["id"] == id_p:
            x["status"] = "Dibatalkan"
    simpan_pesan(semua)

    tikets = baca_tiket()
    for t in tikets:
        if t["id"] == p["id_tiket"]:
            t["tersedia"] = str(int(t["tersedia"]) + int(p["jumlah"]))
    simpan_tiket(tikets)
    print("  Pemesanan dibatalkan, kuota dikembalikan.")
    jeda()

# =============================

# ── LAPORAN ────────────────────────────────────────

def laporan(): # membuat Laporan
    clear()
    print("=== LAPORAN ===\n")
    tikets  = baca_tiket()
    pesanan = [p for p in baca_pesan() if p["status"] == "Aktif"]

    print(f"  Jumlah event    : {len(tikets)}")
    print(f"  Pemesanan aktif : {len(pesanan)}")
    print(f"  Tiket terjual   : {sum(int(p['jumlah']) for p in pesanan)}")
    print(f"  Total pendapatan: {rp(sum(int(float(p['total'])) for p in pesanan))}")

    print("\n  Stok tiket:")
    for t in bubble_sort(tikets, "tersedia"):
        sisa  = int(t["tersedia"])
        kuota = int(t["kuota"])
        pct   = int(sisa / kuota * 10) if kuota else 0
        bar   = "█" * pct + "░" * (10 - pct)
        print(f"  {t['event']:<22} [{bar}] {sisa}/{kuota}")
    jeda()


# ── MENU ───────────────────────────────────────────

def menu_tiket():  # Menu tiket 
    while True:
        clear()
        print("=== MANAJEMEN TIKET ===\n")
        print("  1. Lihat tiket")
        print("  2. Tambah tiket")
        print("  3. Update tiket")
        print("  4. Hapus tiket")
        print("  5. Cari tiket")
        print("  0. Kembali")
        p = input("\n  Pilih: ").strip()
        if p == "1":   lihat_tiket()
        elif p == "2": tambah_tiket()
        elif p == "3": update_tiket()
        elif p == "4": hapus_tiket()
        elif p == "5": cari_tiket()
        elif p == "0": break


def menu_pemesanan(): # Menu Pemesanan
    while True:
        clear()
        print("=== MANAJEMEN PEMESANAN ===\n")
        print("  1. Lihat pemesanan")
        print("  2. Buat pemesanan")
        print("  3. Update data pemesan")
        print("  4. Batalkan pemesanan")
        print("  0. Kembali")
        p = input("\n  Pilih: ").strip()
        if p == "1":   lihat_pemesanan()
        elif p == "2": buat_pemesanan()
        elif p == "3": update_pemesanan()
        elif p == "4": batalkan_pemesanan()
        elif p == "0": break


def main():  # Menu Utama
    inisialisasi()
    while True:
        clear()
        print("=== SISTEM PEMESANAN TIKET EVENT ===\n")
        print("  1. Manajemen Tiket")
        print("  2. Manajemen Pemesanan")
        print("  3. Laporan")
        print("  4. Reset data awal")
        print("  0. Keluar")
        p = input("\n  Pilih: ").strip()
        if p == "1":   menu_tiket()
        elif p == "2": menu_pemesanan()
        elif p == "3": laporan()
        elif p == "4": reset_data(); jeda()
        elif p == "0": print("\n  Sampai jumpa.\n"); break


if __name__ == "__main__":
    main()
