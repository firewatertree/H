shoping_amount=float(input('enter your shoping_amount:'))
membership_level=input('enter your membership_level (gold or regular):')

if membership_level=='regular': #判斷會員等級
	
	if 1000>shoping_amount:
		print(shoping_amount,'regular')
	
	elif 2000>shoping_amount>1000: #價格範圍判斷
		price=shoping_amount*0.9
		print(price,'regular')
	elif 3000>shoping_amount>2000:
		price=shoping_amount*0.85
		print(price,'regular')
	if shoping_amount>3000:
		price=shoping_amount*0.8
		print(price,'regular')

elif membership_level=='gold':

	if 1000>shoping_amount:
		print(shoping_amount,'gold')
	if 2000>shoping_amount>1000:
		price=shoping_amount*0.85
		print(price,'gold')
	if 3000>shoping_amount>2000:
		price=shoping_amount*0.8
		print(price,'gold')
	if shoping_amount>3000:
		price=shoping_amount*0.75
		print(price,'gold')
else:
	print("invalid input ")
		

#考試時沒有設定如過金額小於1000時的狀況,還有價格範圍沒用好變成輸入3000時全部價格都跑出來  迴圈分成兩個