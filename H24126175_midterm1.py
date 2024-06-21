layer=1 #分成三層處理
while layer <=3: #
    if layer==1:
        j = 9 #設定初始值
        while j >= 1 :#讓他在乘法表末尾停止
            i=9 #設定初始值
            while i >=7:#讓產出可以照題目排序
                print(j,' x ', i, ' = ', end='')
                print('%-3d' % (j * i), end='')
                i-=1
            print(' ')
            j-=1
        print(' ')
    elif layer == 2:  #以下同上
        j = 9
        while j >= 1:
            i = 6
            while i >= 4:
                print(j, ' x ', i, ' = ', end='')
                print('%-3d' % (j * i), end='')
                i-=1
            print(' ')
            j-=1
        print(' ')
    else: #以下同上
        j = 9
        while j >= 1:
            i = 3
            while i >= 1:
                print(j, ' x ', i, ' = ', end='')
                print('%-3d' % (j * i), end='')
                i-=1
            print(' ')
            j-=1
        print(' ')
    layer+=1