# Tugas Kecil 2 Strategi Algoritma
# Membangun Kurva Bezier dengan Algoritma Titik Tengah berbasis Divide and Conquer (Utama) serta Brute Force (Alternatif)

### Dibuat oleh:
| Nama | NIM |
| -------- | --------- |
| Nicholas Reymond Sihite | 13522144 |

## Deskripsi Program
Program ini adalah program yang dibuat untuk menggambar kurva Bezier dengan algoritma Divide and Conquer sebagai algoritma utama dan
algoritma Brute Force sebagai algoritma alternatif. Program ini diimplementasikan dengan bahasa Python. Program akan menampilkan proses pembuatan
kurva Bezier secara step-by-step dengan algoritma Divide and Conquer. Selain itu, program juga akan menampilkan perbandingan waktu eksekusi
kedua algoritma. Setelah itu, program juga dapat membandingkan hasil kurva kedua algoritma secara side-to-side comparison.
(Tambahan: Program dapat menyimpan hasil kurva Bezier per iterasi sebagai file GIF)

## Requirement Program
Module yang butuh instalasi: PIL dan matplotlib\n
   Cara install PIL:
   ```sh
   pip install Pillow
   ```
   Cara install matplotlib:
   ```sh
   pip install matplotlib
   ```

## Cara Menggunakan Program
1. Clone repository dengan cara membuka terminal lalu masukkan perintah berikut
   ```sh
   git clone https://github.com/nicholasrs05/Tucil2_13522144.git
   ```
2. Buka folder "bin" lalu buka file "bezier.exe" (jika ingin melakukan compile sendiri atau file .exe tidak bekerja, lihat poin 7)
3. Masukkan banyaknya titik, titik-titik, dan banyaknya iterasi dengan format berikut
    ```sh
    nPoints
    x1 y1
    x2 y2
    ...
    xn yn
    nIterations
    ```
4. Program akan menampilkan hasil setiap iterasi mulai dari 0 sampai nIterations beserta step-by-step cara kurva digambar. Selain itu,
   program juga akan menampilkan waktu eksekusi pencarian titik-titik dengan algoritma Divide and Conquer dan Brute Force
5. Jika ingin mengunjungi iterasi lain, tutup kurva lalu masukkan nomor iterasi pada program.
6. Program dapat menyimpan hasil kurva Bezier untuk setiap iterasi jika diinginkan. File .gif akan berada pada folder "test"
7. Kompilasi dilakukan dengan masuk ke folder "src", buka terminal, lalu masukkan perintah berikut
    ```sh
    py bezier.py
    ```