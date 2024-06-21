'''
用LIST的資料生成平均值
'''
loop=True
while loop:
    choice_subject=input('Chpoce the subject you want.(math,chinese,art): ')
    if choice_subject=='math':
        math_score = [90, 95, 65, 75]
        i=0
        total=0
        while i<len(math_score):
            total+=math_score[i]
            i=i+1
        print('average math score =',total/len(math_score))

    elif choice_subject=='chinese':
        chinese = [60, 59, 75, 95]
        i = 0
        total = 0
        while i < len(chinese):
            total += chinese[i]
            i = i + 1
        print('average chinese score =', total / len(chinese))
    elif choice_subject=='art':
        art = [46, 53, 32, 100]
        i = 0
        total = 0
        while i < len(art):
            total += art[i]
            i = i + 1
        print('average art score =', total / len(art))
    else:
        print('invalid value please enter you subject again')

    choice=input("do you want another subject's average score.(yes or no): ")

    if choice=='yes':
        print('ok')
    elif choice=='no':
        break
    else:
        print('invalid inout please enter yes or no')


