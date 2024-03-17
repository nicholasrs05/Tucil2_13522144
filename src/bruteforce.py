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

