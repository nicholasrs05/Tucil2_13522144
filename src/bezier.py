import time as t
import functions as f
import divandconq as dac
import bruteforce as bf
import io
from PIL import Image

print("\n\nSELAMAT DATANG DI PROGRAM PEMBUAT KURVA BEZIER DENGAN ALGORITMA DIVIDE AND CONQUER / BRUTE FORCE\n\n")

# Inisiasi variabel
arrIterations = []
arrPoints = []
arrControl = []

# Input banyaknya titik
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

# Input banyaknya iterasi
valid = False
while not (valid):
    try:
        print("\nMasukkan banyaknya iterasi")
        iterations = int(input(">> "))
        valid = True
    except ValueError:
        print("Tolong masukkan bilangan bulat (integer)!")

# Input algoritma yang ingin digunakan
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
        arrControl = dac.createNewControl(arrControl, countPoints)
        for j in range (0, len(arrControl), countPoints - 1):
            arrPoints.append(arrControl[j])
        arrIterations.append(arrPoints)

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
for points in arrIterations:
    f.plot.clf()
    f.plot_bezier_curve(points)

f.plot.ioff()
f.plot.show()

berhenti = False
while not (berhenti):
    try:
        print("Masukkan nomor iterasi yang ingin ditampilkan (-1 untuk berhenti)")
        number = int(input(">> "))
        if (number == -1):
            berhenti = True
        else:
            points = arrIterations[number]
            f.plot_bezier_curve(points)
    except IndexError:
        print(f"Masukkan nomor iterasi pada range 0 - {iterations}")
    except ValueError:
        print("Input tidak valid.")

# Menyimpan file
valid = False
while not (valid):
    print("\nApakah Anda ingin menyimpan hasil dalam format .gif? (Ya/Tidak)")
    strInput = str(input(">> "))
    if ((strInput == "Ya") or (strInput == "Tidak")):
        valid = True
    else:
        print("Masukan tidak valid!")

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
    print(".", end = "")
    t.sleep(1)