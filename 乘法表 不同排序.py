layer=1
while layer <=3:
    if layer==1:
        i = 1
        while i <= 9 :
            j=9
            while j >0:
                print(j,' x ', i, ' = ', end='')
                print('%-3d' % (j * i), end='')
                j-=3
            print(' ')
            i+=1
        print(' ')
    elif layer == 2:
        i = 1
        while i <= 9:
            j = 8
            while j > 0:
                print(j, ' x ', i, ' = ', end='')
                print('%-3d' % (j * i), end='')
                j-=3
            print(' ')
            i+=1
        print(' ')
    else:
        i = 1
        while i <= 9:
            j = 7
            while j > 0:
                print(j, ' x ', i, ' = ', end='')
                print('%-3d' % (j * i), end='')
                j-=3
            print(' ')
            i+=1
        print(' ')
    layer+=1




















