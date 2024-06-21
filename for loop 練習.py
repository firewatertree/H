#請使用 FOR LOOP 計算並輸出從 1 到 10 的所有偶數。
nu=[1,2,3,4,5,6,7,8,9,10]
for i in nu:
    if i % 2==0: #一開始用/會跑不出東西 要用%才能查看是否為偶數
        print(i)
    else:
        continue

#寫一個程式，使用 FOR 迴圈找出一個給定數字的所有因數。
input_number=int(input('Enter the value you want: '))
for i in range(1,input_number+1):
    if input_number % i == 0 :
        print(i)
#寫一個程式，使用 FOR 迴圈計算並列印出給定數字的所有質因數

def prime_factor(n):
    factor=[]
    while n%2 == 0:
        factor.append(2)
        n=n//2
    for i in range(3 , int(n**0.5+1),2):
        while n % i == 0:
            factor.append(i)
            n = n // i
    if n >2:
        factor.append(n)
    return factor

in_number=int(input('enter the number you want: '))
print('質因數是', prime_factor(in_number))

'''
寫一個程式，使用巢狀的 FOR 迴圈來產生以下的圖案：
*
**
***
****
*****
你需要用兩個巢狀的 FOR 迴圈來控制行和列。第一個 FOR 迴圈控制行數，第二個 FOR 迴圈控制列數。在每一行，你需要印出相應數目的星號。

'''
for i in range(1, 6):  # 控制行數
    for j in range(i):  # 控制列數
        print('*', end='')
    print()

'''
寫一個程式，使用 FOR 迴圈來印出下面的菱形模式：
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
row=5
for i in range(1,row+1):
    print(' ' * (row-i),'*'*(2*i-1))  #''只這樣打不會跑出空格 ' ' 中間加空格才行
for j in range(row-1,0,-1):
    print(' ' * (row-j),'*'*(2*j-1))






