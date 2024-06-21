student_number = int(input('Enter the total number of students (n>0): '))
id_list = [1]
i = 1
while student_number > 0:
    if max(id_list) < student_number:
        i += 1
        id_list.append(i)

    if len(id_list) > 2:
        del id_list[2]

    student_number -= 1  # 每次迴圈處理一個學生

print('The last ID is:', id_list[-1])
