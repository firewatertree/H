import random

word_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alphabet=random.choice(word_list) #從字母列表中隨機選出字母
Guess_histogram = [0,0,0,0,0,0,0] #存放猜過的數字
count = 0  # 計算次數的初始值
print(Alphabet)
while True:
    guess=input('Guess the lowercase alphabet: ')#讓使用者輸入想猜的數字
    diff = (ord(guess) - ord("a")) // 4  # -> corresponding pair index
    Guess_histogram[diff] += 1

    if guess == Alphabet :#如果猜對則結束迴圈
        count+=1

        print('Congraduation! You guessed the alphabet',Alphabet,'in',count,'tries')

        break # 結束迴圈
    elif guess != Alphabet:#猜錯則判斷位置是比ALPHABET 大還是小

        if word_list.index(guess) < word_list.index(Alphabet):
            count += 1  # 計算次數

            print('The alphabet you are looking for is alphabetically higher.')

        elif word_list.index(guess) > word_list.index(Alphabet):
            count += 1

            print('The alphabet you are looking for is alphabetically lower. ')

print("guess Histogram")
print(Guess_histogram)
print(f"a - d: {'*' * Guess_histogram[0]}")
print(f"e - h: {'*' * Guess_histogram[1]}")
print(f"i - l: {'*' * Guess_histogram[2]}")
print(f"m - p: {'*' * Guess_histogram[3]}")
print(f"q - t: {'*' * Guess_histogram[4]}")
print(f"u - x: {'*' * Guess_histogram[5]}")
print(f"y - z: {'*' * Guess_histogram[6]}")



