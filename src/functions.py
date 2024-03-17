import matplotlib.pyplot as plot

# Menggambar kurva berdasarkan points
def plot_bezier_curve(points, index):
    # Memisahkan nilai x dan y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar kurva
    plot.plot(x_values, y_values, label = "Kurva Bezier")
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title(f'Kurva Bezier iterasi ke-{index}')
    plot.axis('equal')
    plot.draw()
    plot.pause(1)

def plot_control_points(points):
    # Memisahkan nilai x dan y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar kurva
    plot.plot(x_values, y_values, label = "")
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Kurva Bezier')
    plot.axis('equal')
    plot.draw()
    plot.pause(0.5)

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
    plot.pause(0.5)

def plot_curve(points):
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

def plot_midpoints(points, control):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar titik-titik
    plot.plot(x_values, y_values, marker='o', linestyle='')
    
    i = 0
    while (i < (len(points) - control + 1)):
        temp = []
        for j in range (i, i + control):
            temp.append(points[j])
        plot_curve(temp)
        i = i + control

    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Kurva Bezier')
    plot.axis('equal')
    plot.draw()
    plot.pause(0.5)