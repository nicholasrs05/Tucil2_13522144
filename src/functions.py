import matplotlib.pyplot as plot

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

def plot_points_only(points):
    # Memisahkan nilai x dan y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar titik-titik
    plot.plot(x_values, y_values, marker='o', linestyle='')
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Kurva Bezier')
    plot.axis('equal')
    plot.draw()
    plot.pause(1)