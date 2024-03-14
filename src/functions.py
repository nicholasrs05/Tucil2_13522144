import matplotlib.pyplot as plot

def insertSort(arrPoints, Point):
    idx = 0
    while (idx < len(arrPoints) and (arrPoints[idx][0] < Point[0])):
        idx += 1
    if (Point) not in (arrPoints):
        arrPoints.insert(idx, Point)
    return arrPoints

def plot_bezier_curve(points):
    # Separating x and y values
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # menggambar kurva
    plot.plot(x_values, y_values)
    plot.xlabel('Sumbu x')
    plot.ylabel('Sumbu y')
    plot.title('Kurva Bezier')
    # plot.grid(True)
    plot.axis('equal')
    plot.gca().set_aspect('equal')
    # plot.xlim(min(x_values), max(x_values))
    # plot.ylim(min(y_values), max(y_values))
    plot.show()