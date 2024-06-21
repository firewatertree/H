sum=0
now=1
n=int(input('enter an avalue'))
while now <= n:
	sum += now
	now += 1
print('sum up 1 to',n,'=',sum)

password=''
while password!='abcdbitch':
	password=input('please enter the password:')
	if password=='abcdbitch':
		print('thank you')
	else:
	    print('sorry')	

t=0
pop=3333
r=0.57
while pop<33330:
	pop+=pop**r
	print(pop)
	t+=1
print('took',t,'minute for bacteria to gorws ten times large')
print('and the final population is',pop)
