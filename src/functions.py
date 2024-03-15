import matplotlib.pyplot as plot

# Memasukkan Point ke arrPoints dengan terurut tanpa ada pengulangan
def insertSort(arrPoints, Point):
    idx = 0

    # Mencari index
    while (idx < len(arrPoints) and (arrPoints[idx][0] < Point[0])):
        idx += 1
    
    # Memasukkan Point ke arrPoints jika belum ada
    if (Point) not in (arrPoints):
        arrPoints.insert(idx, Point)
    
    return arrPoints

# Menggambar kurva berdasarkan points
def plot_bezier_curve(points):
    # Memisahkan nilai x dan y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar kurva
    plot.plot(x_values, y_values)
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Kurva Bezier')
    plot.axis('equal')
    plot.draw()
    plot.pause(1)