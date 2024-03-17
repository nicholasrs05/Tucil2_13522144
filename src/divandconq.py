def createNewControl(prevControl, cntControl):
    # ---- DIVIDE AND CONQUER ----
    # Membagi titik-titik control menjadi beberapa bagian dengan 1 bagian berjumlah cntControl titik
    # Contoh:
    # cntControl = 3
    # prevControl = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    # prevControl dibagi menjadi [(1, 1), (2, 2), (3, 3)] dan [(3, 3), (4, 4), (5, 5)]
    # Lalu setiap bagian digunakan untuk membuat titik kontrol baru

    newControl = []
    arrMidPoints = [[] for i in range (cntControl)]
    arrMidPoints[0] = prevControl.copy()
    i = 0

    while (i < (len(prevControl) - cntControl + 1)):
        idx = 0
        temp = []
        saveControl = []

        # Meyimpan bagian ke-(i + 1)
        for j in range (i, i + cntControl):
            temp.append(prevControl[j])

        # Menyimpan titik-titik ujung
        saveControl.append(prevControl[i])
        saveControl.append(prevControl[i + (cntControl - 1)])
        idx = idx + 1

        # Loop untuk membuat dan menyimpan titik kontrol baru
        while (len(temp) != 1):
            temp2 = []

            # Mencari titik-titik tengah temp
            for k in range (len(temp) - 1):
                x = float((temp[k][0] + temp[k + 1][0]) / 2)
                y = float((temp[k][1] + temp[k + 1][1]) / 2)
                temp2.append((x, y))

                # Menyimpan titik tengah untuk menggambar kurva step-by-step
                if ((x, y)) not in (arrMidPoints[idx]):
                    arrMidPoints[idx].append((x, y))

            temp = temp2.copy()

            # Menyimpan titik tengah paling kiri dan paling kanan
            # Contoh: temp = [(1.5, 1.5), ...,  (2.5, 2.5)]
            # (1.5, 1.5) dan (2.5, 2.5) akan diinsert di tengah saveControl
            saveControl.insert(idx, temp[0])
            saveControl.insert(len(saveControl) - idx, temp[-1])

            idx = idx + 1
            # Loop dilanjutkan sampai hanya ada 1 elemen temp, yaitu titik baru yang akan dijadikan bagian dari kurva

        # Memasukkan titik kontrol bagian ini ke array penyimpanan titik kontrol yang baru, yaitu newControl
        for j in range (len(saveControl)):
            if (saveControl[j]) not in (newControl):
                newControl.append(saveControl[j])

        # Melanjutkan ke bagian berikutnya
        i = i + (cntControl - 1)

    return [newControl, arrMidPoints]