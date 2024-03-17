def createNewControl(prevControl, cntControl):
    newControl = []
    newControl.append(prevControl[0])
    i = 0

    while (i < (len(prevControl) - cntControl + 1)):
        idx = 0
        temp = []
        saveControl = []
        for j in range (i, i + cntControl):
            temp.append(prevControl[j])

        saveControl.append(prevControl[i])
        saveControl.append(prevControl[i + (cntControl - 1)])
        idx = idx + 1

        while (len(temp) != 1):
            temp2 = []

            for k in range (len(temp) - 1):
                x = float((temp[k][0] + temp[k + 1][0]) / 2)
                y = float((temp[k][1] + temp[k + 1][1]) / 2)
                temp2.append((x, y))

            temp = temp2.copy()
            saveControl.insert(idx, temp[0])
            saveControl.insert(len(saveControl) - idx, temp[-1])
            idx = idx + 1

        for j in range (len(saveControl)):
            if (saveControl[j]) not in (newControl):
                newControl.append(saveControl[j])
        i = i + (cntControl - 1)

    return newControl