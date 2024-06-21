s=input('enter a positive integer: ')

l=[]
i=0
while i<len(s):
    l=l+[int(s[i])]
    i=i+1
print(l)

new_list=[]
i=0
while i <len(l):
    if i == 0:
        new_list=new_list + [sum(l[0:2])]
    elif i == len(l)-1:
        new_list=new_list + [sum(l[len(l)-2:len(l)])]
    else:
        new_list = new_list + [sum(l[i-1:i+2])]
    i=i+1
print(new_list)

