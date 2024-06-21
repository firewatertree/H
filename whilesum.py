def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(x):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < x:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    if fib_sequence[-1] == x:
        return len(fib_sequence)
    return False

def find_prime(x):
    count = 0
    num = 2
    while count < x:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1

while True:
    try:
        x = int(input("Enter a positive integer greater than 1: "))
        if x <= 1:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer greater than 1.")

fibonacci_index = fibonacci(x)
if fibonacci_index:
    print(f"{x} is the {fibonacci_index}th number in Fibonacci sequence.")
else:
    print(f"{x} is not in Fibonacci sequence.")

prime_number = find_prime(x)
print(f"The {x}th Prime number is {prime_number}.")


