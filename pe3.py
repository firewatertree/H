print('Welcome to the simple calculator program !')
loop = True
'''這段程式碼是一個無限迴圈的開始部分。通過設置 loop = True，它創建了一個條件，使得 while 迴圈的條件始終為真。

while loop: 這一行的意思是，當 loop 變數的值為真（即 True）時，迴圈會持續執行下去。因為 loop 被設置為 True，這個條件將永遠成立，因此這個迴圈將無限循環下去，直到有特定的條件導致 loop 變為 False。

在這樣的設置下，迴圈可能會在某些地方需要一個終止條件或者在迴圈體內使用 break 語句，否則將永遠運行下去，直到強制終止程式執行。
'''
while loop:

    answer1 = float(input('Enter the first number: '))
    answer2 = float(input('Enter the second number: '))
    answer3 = input('Select an arithmetic operation (+, -, *, /): ')
    if answer3 == '+':
        result = answer1 + answer2

    elif answer3 == '-':
        result = answer1 - answer2

    elif answer3 == '*':
        result = answer1 - answer2

    elif answer3 == '/':
        if answer2 == 0: #我在0加了'' 系統無法判斷跑不出來
            print('division zero please input number again')
            continue
        else:
            result = answer1 / answer2

    print('result',result)

    choice = input('Do you want to perform another calculation? (yes or no): ')
    if choice == 'no':
        break
    elif choice == 'yes':
        print('ok')
    else:
        print('invalid input')