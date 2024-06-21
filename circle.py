student_number=int(input('enter the total number of students (n>0): '))
id_list = [1]
i=1
if student_number > 0 :

    if max(id_list) < student_number:
        i+=1
        id_list.append(i)


    if len(id_list) > 1:
        del id_list[2]
    student_number-=1

    print('The last ID is : ',id_list)
elif student_number ==0 :
    print('Invalid value enter again')




