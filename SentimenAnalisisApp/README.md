# Deskripsi Pengujian

| Objek Pengujian | Hasil      | Lampiran                                      |
| --------------- | ---------- | --------------------------------------------- |
| Delete Sentimen | Berhasil ✔ | [dokumentasi](./LaporanTesting_AdeCandra.pdf) |

# Panduan Penggunaan

Ini adalah kode Python untuk melakukan pengujian otomatis pada aplikasi web menggunakan Selenium.

## Persyaratan

Sebelum menggunakan kode ini, pastikan Anda telah memenuhi persyaratan berikut:

- Python 3.x terpasang di sistem Anda.
- WebDriver yang sesuai untuk browser yang ingin Anda gunakan (contoh: ChromeDriver untuk Google Chrome).

## Instalasi

1. Clone repositori ini ke dalam sistem Anda:

   ```
   git clone <link-repositori>
   ```

2. Instal selenium dengan menjalankan perintah berikut di terminal:

   ```
   pip install selenium
   ```

3. Pastikan WebDriver telah diunduh dan tersedia di PATH sistem Anda.

## Penggunaan

1. Buka file `delsentimen.py` dan lakukan modifikasi sesuai dengan kebutuhan Anda, seperti URL halaman web yang ingin diuji, informasi login, dll. Sesuaikan path lokasi file sebelumkan menjalankan pengujian.

2. Jalankan pengujian dengan menjalankan perintah berikut di terminal:

   ```
   python delsentimen.py
   ```

3. Tunggu hingga pengujian selesai dieksekusi. Hasil pengujian akan ditampilkan di terminal.
