import matplotlib.pyplot as plot

# Menggambar kurva berdasarkan points
def plot_bezier_curve(points, index, max_val, min_val):
    # Memisahkan nilai x dan y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar kurva
    plot.plot(x_values, y_values, label = "Kurva Bezier")
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title(f'Kurva Bezier iterasi ke-{index}')
    plot.axis([min_val, max_val, min_val, max_val])
    plot.axis('equal')
    plot.draw()
    plot.pause(1)

def plot_control_points(points, max_val, min_val):
    # Memisahkan nilai x dan y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar kurva
    plot.plot(x_values, y_values, label = "")
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Kurva Bezier')
    plot.axis([min_val, max_val, min_val, max_val])
    plot.axis('equal')
    plot.draw()
    plot.pause(0.5)

def plot_points_only(points, max_val, min_val):
    # Memisahkan nilai x dan y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar titik-titik
    plot.plot(x_values, y_values, marker='o', linestyle='')
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Kurva Bezier')
    plot.axis([min_val, max_val, min_val, max_val])
    plot.axis('equal')
    plot.draw()
    plot.pause(0.5)

def plot_curve(points, max_val, min_val):
    # Memisahkan nilai x dan y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar kurva
    plot.plot(x_values, y_values)
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Kurva Bezier')
    plot.axis([min_val, max_val, min_val, max_val])
    plot.axis('equal')
    plot.draw()

def plot_midpoints(points, control, max_val, min_val):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Gambar titik-titik
    plot.plot(x_values, y_values, marker='o', linestyle='')
    
    i = 0
    while (i < (len(points) - control + 1)):
        temp = []
        for j in range (i, i + control):
            temp.append(points[j])
        plot_curve(temp, max_val, min_val)
        i = i + control

    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Kurva Bezier')
    plot.axis([min_val, max_val, min_val, max_val])
    plot.axis('equal')
    plot.draw()
    plot.pause(0.5)

def draw_two_curve(points1, points2, max_val, min_val):
    plot.figure(figsize=(10, 5))
    plot.subplot(1, 2, 1)
    plot_curve(points1, max_val, min_val)
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Divide and Conquer')
    plot.axis([min_val, max_val, min_val, max_val])
    plot.axis('equal')

    plot.subplot(1, 2, 2)
    plot_curve(points2, max_val, min_val)
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Brute Force')
    plot.axis([min_val, max_val, min_val, max_val])
    plot.axis('equal')

    plot.tight_layout()
    plot.show()

def plot_points_with_coordinates(points, max_val, min_val):
    # Extract x and y coordinates from points
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Plot points
    plot.scatter(x_values, y_values)

    # Annotate each point with its coordinates
    for point in points:
        plot.annotate(f'({point[0]}, {point[1]})', xy = point, textcoords = 'offset points', xytext = (5,5), ha = 'left')
    plot_curve(points, max_val, min_val)

    # Set labels and title
    plot.xlabel('X')
    plot.ylabel('Y')
    plot.title('Plot with Point Coordinates')

    # Show plot
    plot.show()