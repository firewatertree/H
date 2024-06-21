def is_perfect_number(num):
    # 找到 num 的所有真因數，並計算它們的和
    sum_of_factors = sum([i for i in range(1, num) if num % i == 0])
    # 檢查是否為完美數
    return sum_of_factors == num

def find_perfect_numbers(range_end):
    perfect_numbers = []
    for i in range(2, range_end + 1):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers

input_range = int(input("請輸入範圍的上限："))
perfect_numbers_in_range = find_perfect_numbers(input_range)
print("在範圍內的完美數：", perfect_numbers_in_range)
