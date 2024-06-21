


thief=1
while thief<=4:
	cnt=0
	if(thief!=1):
	  cnt+=2
	if(thief==3):
		cnt+=2
	if(thief==2):
		cnt+=3
	if(thief==4):
		cnt+=1
	if(thief!=4):
		cnt+=1
	if(thief==3):
		print("the thief is", thief)
	thief=thief+1
	
