# Tugas Kecil 2 Strategi Algoritma
# Membangun Kurva Bezier dengan Algoritma Titik Tengah berbasis Divide and Conquer (Utama) serta Brute Force (Alternatif)

### Dibuat oleh:
| Nama | NIM |
| -------- | --------- |
| Nicholas Reymond Sihite | 13522144 |

## Deskripsi Program
Program ini adalah program yang dibuat untuk menggambar kurva Bezier dengan algoritma Divide and Conquer sebagai algoritma utama dan
algoritma Brute Force sebagai algoritma alternatif. Program ini diimplementasikan dengan bahasa Python.

## Cara Menggunakan Program
1. Clone repository dengan cara membuka terminal lalu masukkan perintah berikut
   ```sh
   git clone https://github.com/nicholasrs05/Tucil2_13522144.git
   ```
2. Buka folder "bin" lalu buka file "main.exe" (jika ingin melakukan compile sendiri, lihat poin 5)
3. Masukkan banyaknya titik, titik-titik, dan banyaknya iterasi dengan format berikut
    ```sh
    nPoints
    x1 y1
    x2 y2
    ...
    xn yn
    nIterations
    ```
4. Program akan menampilkan hasil setiap iterasi mulai dari 0 sampai nIterations. Jika ingin mengunjungi iterasi sebelumnya, tutup kurva lalu masukkan nomor iterasi pada program.
5. Kompilasi dilakukan dengan masuk ke folder "src", buka terminal, lalu masukkan perintah berikut
    ```sh
    py bezier.py
    ```