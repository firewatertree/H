x = int(input('enter x: '))
y = int(input('enter y: '))
if x <= y:
    number=x
    bound=y
else:
    number=y
    bound=x
result=''
while number <= bound:
    if (number %13 == 0) and (number % 7 == 0):
        result=result+"  "+ str(number) + ''
    number+=1
print(result)

