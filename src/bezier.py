import functions as f

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
    else:
        arrControl.append((float(x), float(y)))

# Menambahkan array titik ke array iterasi agar dapat ditampilkan per iterasi
arrIterations.append(arrPoints)

# Input banyaknya iterasi
iterations = int(input("Masukkan banyaknya iterasi: "))

# Loop setiap iterasi
for i in range (iterations):
    # Titik lama
    arrPoints = arrIterations[i].copy()

    # Kontrol lama
    temp = arrControl

    # Gabungkan titik lama dan kontrol lama
    for j in range (len(arrPoints)):
        temp = f.insertSort(temp, arrPoints[j])
    
    tempControl = []

    # Titik tengah antara titik dan kontrol
    for j in range (len(temp) - 1):
        x = float((temp[j][0] + temp[j + 1][0]) / 2)
        y = float((temp[j][1] + temp[j + 1][1]) / 2)
        tempControl.append((x, y))
    
    # Menyimpan titik kontrol untuk penggunaan di iterasi selanjutnya
    arrControl = tempControl

    for j in range (len(tempControl) - 1):
        x = float((tempControl[j][0] + tempControl[j + 1][0]) / 2)
        y = float((tempControl[j][1] + tempControl[j + 1][1]) / 2)
        arrPoints = f.insertSort(arrPoints, (x, y))
    
    # Menyimpan titik-titik ke array agar dapat ditampilkan
    arrIterations.append(arrPoints)

# Mengambil array titik pada iterasi terakhir
f.plot.ion()

# Menggambar setiap iterasi titik
for points in arrIterations:
    f.plot.clf()
    f.plot_bezier_curve(points)

f.plot.ioff()
f.plot.show()

while True:
    try:
        number = int(input("Masukkan nomor iterasi yang diinginkan (-1 untuk berhenti): "))
        if (number == -1):
            break
        else:
            points = arrIterations[number]
            f.plot_bezier_curve(points)
    except IndexError:
        print(f"Masukkan nomor iterasi pada range 0 - {number}")
    except ValueError:
        print("Input tidak valid.")