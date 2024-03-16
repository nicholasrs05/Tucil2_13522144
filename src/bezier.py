import time as t
import functions as f
import divandconq as dac
import bruteforce as bf

# Inisiasi variabel
arrIterations = []
arrPoints = []
arrControl = []

# Input banyaknya titik
countPoints = int(input("Masukkan banyaknya titik: "))

# Loop menerima input titik
for i in range (countPoints):
    x, y = input().split()
    if (i == 0) or (i == countPoints - 1):
        arrPoints.append((float(x), float(y)))
    arrControl.append((float(x), float(y)))

# Menambahkan array titik ke array iterasi agar dapat ditampilkan per iterasi
arrIterations.append(arrPoints)

# Input banyaknya iterasi
iterations = int(input("Masukkan banyaknya iterasi: "))

# Input algoritma yang ingin digunakan
accept = False
print("Mau dibuat dengan algoritma apa?")
print("1. Divide and Conquer")
print("2. Brute Force")

while not (accept):
    strInput = str(input("Silakan masukkan nomor ATAU nama algoritma (case sensitive): "))
    if ((strInput == "1") or (strInput == "2") or (strInput == "Divide and Conquer") or (strInput == "Brute Force")):
        accept = True
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
print(f"Waktu eksekusi algoritma: {endTime - startTime} detik")

# Inisiasi kurva
f.plot.ion()

# Menggambar setiap iterasi titik
for points in arrIterations:
    f.plot.clf()
    f.plot_bezier_curve(points)

f.plot.ioff()
f.plot.show()

while True:
    try:
        number = int(input("Masukkan nomor iterasi yang ingin ditampilkan (-1 untuk berhenti): "))
        if (number == -1):
            break
        else:
            points = arrIterations[number]
            f.plot_bezier_curve(points)
    except IndexError:
        print(f"Masukkan nomor iterasi pada range 0 - {iterations}")
    except ValueError:
        print("Input tidak valid.")