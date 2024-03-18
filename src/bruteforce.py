# Membuat segitiga pascal
def createPascalTriangle(level):
    if (level == 0):
        return [1]
    elif (level == 1):
        return [1, 1]
    else:
        prev = createPascalTriangle(level - 1)
        curr = [1]
        for i in range (len(prev) - 1):
            curr.append(prev[i] + prev[i + 1])
        curr.append(1)
        return curr

def calculate(arrControl, coefficients, tVal):
    i = 0.0
    savePoints = []
    while (i <= 1.0):
        tempx = 0
        tempy = 0
        for j in range (len(arrControl)):
            x = arrControl[j][0]
            y = arrControl[j][1]
            tempx = tempx + (coefficients[j] * ((1 - i)**(len(arrControl) - 1 - j)) * ((i)**(j)) * x)
            tempy = tempy + (coefficients[j] * ((1 - i)**(len(arrControl) - 1 - j)) * ((i)**(j)) * y)
        savePoints.append((tempx, tempy))
        
        i = i + tVal
    
    return savePoints