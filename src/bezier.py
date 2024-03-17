# PROGRAM MEMBUAT KURVA BEZIER DENGAN ALGORITMA DIVIDE AND CONQUER / BRUTE FORCE
# DIBUAT OLEH:
# Nama  : Nicholas Reymond Sihite
# NIM   : 13522144
# Kelas : K-03 Strategi Algoritma 2024

import time as t
import functions as f
import divandconq as dnc
import bruteforce as bf
import io
from PIL import Image

print("\n\nSELAMAT DATANG DI PROGRAM PEMBUAT KURVA BEZIER DENGAN ALGORITMA DIVIDE AND CONQUER / BRUTE FORCE\n\n")

# Inisiasi variabel
arrIterations = []
arrPoints = []
arrControlIterations = []
arrControl = []

# Input: banyaknya titik
valid = False
while not (valid):
    try:
        print("Masukkan banyaknya titik")
        countPoints = int(input(">> "))
        valid = True
    except ValueError:
        print("Tolong masukkan bilangan bulat (integer)!")

# Loop menerima input titik
print("\nMasukkan titik-titik dengan format:\nx y")
for i in range (countPoints):
    x, y = input().split()
    if (i == 0) or (i == countPoints - 1):
        arrPoints.append((float(x), float(y)))
    arrControl.append((float(x), float(y)))

# Menambahkan array titik ke array iterasi agar dapat ditampilkan per iterasi
arrIterations.append(arrPoints)
arrControlIterations.append(arrControl)

# Input: banyaknya iterasi
valid = False
while not (valid):
    try:
        print("\nMasukkan banyaknya iterasi")
        iterations = int(input(">> "))
        valid = True
    except ValueError:
        print("Tolong masukkan bilangan bulat (integer)!")

arrMidPoints = [[] for i in range (iterations + 1)]

# Input: algoritma yang ingin digunakan
valid = False
print("\nMau dibuat dengan algoritma apa?")
print("1. Divide and Conquer")
print("2. Brute Force")

while not (valid):
    print("\nSilakan masukkan nomor ATAU nama algoritma (case sensitive)")
    strInput = str(input(">> "))
    if ((strInput == "1") or (strInput == "2") or (strInput == "Divide and Conquer") or (strInput == "Brute Force")):
        valid = True
    else:
        print("Masukan tidak valid!")

# Time keeper (start)
startTime = t.time()

# Algoritma Divide and Conquer
if ((strInput == "1") or (strInput == "Divide and Conquer")):
    # Loop setiap iterasi
    for i in range (iterations):
        arrPoints = []

        # Mengambil titik kontrol yang baru
        temp = dnc.createNewControl(arrControl, countPoints)
        arrControl = temp[0].copy()
        arrMidPoints[i + 1] = temp[1].copy()

        # Mengambil titik-titik yang akan digambarkan
        # Contoh:
        # countPoints = 3
        # arrControl = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        # Titik-titik yang akan diambil adalah (1, 1), (3, 3), dan (5, 5)
        for j in range (0, len(arrControl), countPoints - 1):
            arrPoints.append(arrControl[j])

        # Memasukkan titik-titik ke penyimpanan titik setiap iterasi
        arrIterations.append(arrPoints)
        arrControlIterations.append(arrControl)

# Algoritma Brute Force
else:
    print("Coming soon! :)))")

# Time keeper (end)
endTime = t.time()

# Menampilkan waktu eksekusi
print(f"\nWaktu eksekusi algoritma: {endTime - startTime} detik\n")

# Inisiasi kurva
f.plot.ion()

# Menggambar setiap iterasi titik
i = 0
for points in arrIterations:
    f.plot.clf()
    if (i != 0):
        f.plot_points_only(arrControlIterations[i - 1])
        f.plot_control_points(arrControlIterations[i - 1])
    else:
        f.plot_points_only(arrControlIterations[i])
    for j in range (1, len(arrMidPoints[i])):
        f.plot_midpoints(arrMidPoints[i][j], countPoints - j)
    f.plot_points_only(points)
    f.plot_bezier_curve(points, i)
    f.plot.clf()
    f.plot_bezier_curve(points, i)
    i = i + 1

f.plot.ioff()
f.plot.show()

# Menampilkan kurva iterasi
berhenti = False
while not (berhenti):
    try:
        print("Masukkan nomor iterasi yang ingin ditampilkan (-1 untuk berhenti)")
        number = int(input(">> "))
        if (number == -1):
            berhenti = True
        else:
            points = arrIterations[number]
            f.plot_bezier_curve(points, number)
    except IndexError:
        print(f"Masukkan nomor iterasi pada range 0 - {iterations}")
    except ValueError:
        print("Input tidak valid.")

# Input: user ingin menyimpan file atau tidak
valid = False
while not (valid):
    print("\nApakah Anda ingin menyimpan hasil dalam format .gif? (Ya/Tidak)")
    strInput = str(input(">> "))
    if ((strInput == "Ya") or (strInput == "Tidak")):
        valid = True
    else:
        print("Masukan tidak valid!")

# Jika ingin menyimpan file
if (strInput == "Ya"):
    frames = []

    for i, points in enumerate(arrIterations):
        f.plot.plot(*zip(*points))
        f.plot.xlabel('Sumbu x')
        f.plot.ylabel('Sumbu y')
        f.plot.title(f'Iterasi ke-{i}')
        
        buf = io.BytesIO()
        f.plot.savefig(buf, format='png')
        buf.seek(0)
        
        img = Image.open(buf)
        frames.append(img)
        
        f.plot.clf()

    # Input nama file
    print("Masukkan (HANYA) nama file yang diinginkan: ")
    namaFile = str(input(">> "))

    # Simpan sebagai .gif
    frames[0].save(f'test/{namaFile}.gif', format = 'GIF', append_images = frames[1:], save_all = True, duration = 1000, loop = 0)

t.sleep(0.5)
print("\n\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM PEMBUAT KURVA BEZIER :)\n\n")
t.sleep(0.5)

print("Menutup program", end = "")
for i in range (3):
    t.sleep(1)
    print(".", end = "")
t.sleep(1)