i = 1
while i <= 9:  # 遍歷每一行
    j = 1
    while j <= 9:  # 遍歷每一列
        for k in range(i, min(i+3, 10)):  # 控制每行的數字，最多不超過 9
            print("{:2d} x {:2d} = {:2d}".format(k, j, k*j), end='\t')
        print()  # 換行
        j += 1
    print()  # 換行
    i += 3  # 開始下一行

