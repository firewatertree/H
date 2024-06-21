print('Welcome to the simple calculator program !')
loop = True
while loop:

	answer1=float(input('Enter the first number: '))
	answer2=float(input('Enter the second number: '))
	answer3=input('Select an arithmetic operation (+, -, *, /): ')
	if answer3=='+':
		result=answer1 + answer2
		print(result)
	elif answer3=='-':
		result=answer1 - answer2
		print(result)
	elif answer3=='*':
		result=answer1 - answer2
		print(result)
	elif answer3=='/':
		if answer2 != 0:
			result=answer1 / answer2
			print(result)
			
		else :
			print('division zero please input number again')
			answer2=float(input('Enter the second number: '))
			result = answer1 / answer2
			print(result)
		
	choice=input('Do you want to perform another calculation? (yes or no): ')
	if choice=='no':
		break
	elif choice=='yes':
		print('ok')
	else:
		print('invalid input')




		
	



			





	