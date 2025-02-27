n = int(input("Enter the size of the grid: "))

# construct a 2-d matrix with dimension n
matrix = [["_" for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
    # you can also use the below code to replace line 7 ~ line 9
    # print(" ".join(matrix[i]))

cell_coordinate = ""
new_value = ""

while cell_coordinate != "done":
    row, col = 0, 0
    cell_coordinate = input("Enter the cell coordinates to edit: ")
    if cell_coordinate == "done":
        break
    else:
        row, col = cell_coordinate.split(",")
        row, col = int(row), int(col)
    new_value = input("Enter the new value for the cell: ")

    # update the matrix value
    matrix[row][col] = new_value

    for i in range(n):
        print(" ".join(matrix[i]))



