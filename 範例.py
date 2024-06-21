'''
要将从输入中获得的一串数字转换为列表，
你可以使用 split() 方法将输入字符串拆分成单独的数字，
然后将其转换为整数并放入列表中。以下是实现这一目标的示例代码：
'''
# 从输入获取一串数字，以空格分隔
input_string = input("请输入一串数字，以空格分隔：")

# 使用 split() 方法将输入字符串拆分成单独的数字字符串，并存储在列表中
numbers_as_strings = input_string.split()

# 将数字字符串转换为整数，并放入列表中
numbers = [int(num) for num in numbers_as_strings]

# 输出转换后的列表
print("转换后的列表：", numbers)


#不用空格分開版本
# 从输入获取一串数字，没有明确的分隔符
input_string = input("请输入一串数字，没有明确的分隔符：")

# 按照固定长度（例如，每两个字符表示一个数字）将输入字符串拆分成子字符串，并存储在列表中
chunk_size = 1
numbers_as_strings = [input_string[i:i+chunk_size] for i in range(0, len(input_string), chunk_size)]

# 将数字字符串转换为整数，并放入列表中
numbers = [int(num) for num in numbers_as_strings]

# 输出转换后的列表
print("转换后的列表：", numbers)



tom_h,tom_w,tom_a = 1.8,133,70
meng_h,meng_w,meng_a=1.83,70,21

def compute_BMI(height, weight):
    bmi=weight/height**2
    return bmi
def heartrisk(bmi,age):
    table=[['medium','high'],['low','medium']]
    young=age<45

    heavy=bmi>=22

    risk=table[young][heavy]
    return risk
tom_bmi=compute_BMI(tom_h,tom_w)
print('tom:bmi=%.2f,risk=%s'%(tom_bmi,heartrisk(tom_bmi,tom_a)))

