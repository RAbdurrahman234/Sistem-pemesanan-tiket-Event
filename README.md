# Sistem-Pemesanan-Tiket-Event 

Sistem Pemesanan Tiket Event adalah aplikasi berbasis Python yang digunakan untuk mengelola data pemesanan tiket event. Aplikasi ini menerapkan konsep struktur data dan algoritma untuk melakukan pengelolaan data secara efisien, dengan penyimpanan data menggunakan file CSV sebagai database flat file. Pengguna dapat melakukan pemesanan, mencari, melihat, mengubah, menghapus, dan mengurutkan data tiket maupun pemesanan melalui antarmuka Command Line Interface (CLI).

Tujuan Proyek:

1.Menerapkan konsep struktur data dalam pengembangan aplikasi
2.Mengimplementasikan operasi CRUD (Create, Read, Update, Delete)
3.Mengelola data tiket event menggunakan file CSV sebagai database
4.Mengimplementasikan algoritma pencarian (Searching) dan pengurutan (Sorting)
5.Mensimulasikan sistem antrian pemesanan tiket menggunakan Queue berbasis Linked List
6.Membuat aplikasi pemesanan tiket event berbasis CLI yang sederhana dan mudah digunakan

Fitur Utama

1.Pemesanan tiket event
2.Menampilkan seluruh data tiket dan pemesanan
3.Mengubah data tiket maupun data pemesan
4.Membatalkan atau menghapus tiket dan pemesanan
5.Mencari data tiket berdasarkan nama event, lokasi, atau ID
6.Mengurutkan data tiket berdasarkan nama, harga, atau tanggal
7.Mengelola antrian pemesanan tiket
8.Menyimpan dan membaca data dari file CSV
9.Menampilkan laporan dan statistik pemesanan

Struktur Data yang Digunakan:

1.Linked List Queue — digunakan untuk mensimulasikan antrian pemesanan tiket. Fungsi: menambahkan pemesanan ke antrian (enqueue), memproses pemesanan dari antrian (dequeue)
2.Hash Map — digunakan untuk pencarian data tiket berdasarkan ID secara langsung. Fungsi: menyimpan data tiket sementara berdasarkan key ID, mengambil data dengan O(1)

Algoritma yang Digunakan:

1.Bubble Sort — digunakan untuk mengurutkan data tiket berdasarkan nama event, harga, atau tanggal. Cara kerja: membandingkan dua data berdekatan, menukar posisi jika urutan tidak sesuai, diulang hingga seluruh data terurut
2.Binary Search — digunakan untuk mencari data tiket pada data yang sudah terurut. Cara kerja: membagi data menjadi dua bagian, membandingkan nilai tengah dengan target, mempersempit pencarian ke kiri atau kanan hingga data ditemukan

Menu Program:

1.Manajemen Tiket (Lihat, Tambah, Update, Hapus, Cari)
2.Manajemen Pemesanan (Lihat, Buat, Update, Batalkan)
3.Laporan & Statistik
4.Reset Data Awal
5.Keluar
