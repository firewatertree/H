data='from yiqwer314679@gmail.com Tue sep 27 10:14:16 2024'
pos1=data.find('y')
pos2=data.find('@')
data=data[:pos1+1]+'iqwer314679'+data[pos2:]
pos3=data.find('Tue')
modified_data=data[pos3:]+''+data[:pos3]
print(modified_data)