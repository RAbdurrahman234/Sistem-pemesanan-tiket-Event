import csv
import os

TIKET_FILE = "tiket.csv"
PESAN_FILE = "pemesanan.csv"

KOLOM_TIKET = ["id", "event", "tanggal", "lokasi", "harga", "kuota", "tersedia"]
KOLOM_PESAN = ["id", "id_tiket", "pemesan", "email", "jumlah", "total", "waktu", "status"]

DATA_AWAL_TIKET = [
    {"id": "0001", "event": "Konser",             "tanggal": "2026-08-15", "lokasi": "Jakarta",  "harga": "350000", "kuota": "100", "tersedia": "100"},
    {"id": "0002", "event": "Festival",           "tanggal": "2026-09-01", "lokasi": "Bali",     "harga": "250000", "kuota": "80",  "tersedia": "80"},
    {"id": "0003", "event": "Pameran",            "tanggal": "2026-07-20", "lokasi": "Bandung",  "harga": "75000",  "kuota": "200", "tersedia": "200"},
    {"id": "0004", "event": "Seminar",            "tanggal": "2026-08-05", "lokasi": "Surabaya", "harga": "150000", "kuota": "150", "tersedia": "150"},
]


def inisialisasi():
    if not os.path.exists(TIKET_FILE):
        _tulis(TIKET_FILE, KOLOM_TIKET, DATA_AWAL_TIKET)
    if not os.path.exists(PESAN_FILE):
        _tulis(PESAN_FILE, KOLOM_PESAN, [])


def baca_tiket():
    return _baca(TIKET_FILE)

def simpan_tiket(data):
    _tulis(TIKET_FILE, KOLOM_TIKET, data)

def baca_pesan():
    return _baca(PESAN_FILE)

def simpan_pesan(data):
    _tulis(PESAN_FILE, KOLOM_PESAN, data)


def _baca(file):
    with open(file, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def _tulis(file, kolom, data):
    with open(file, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kolom)
        w.writeheader()
        w.writerows(data)


def id_baru(prefix, data):
    angka = []
    for d in data:
        try:
            angka.append(int(d["id"].replace(prefix, "")))
        except:
            pass
    return f"{prefix}{max(angka, default=0) + 1:03d}"


def reset_data(): # menghapus data yang telah dibuat kecuali dari dalam csv di database
    _tulis(TIKET_FILE, KOLOM_TIKET, DATA_AWAL_TIKET)
    _tulis(PESAN_FILE, KOLOM_PESAN, [])
    print("  Data berhasil direset ke kondisi awal.")
