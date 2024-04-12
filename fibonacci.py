def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

num = int(input("Enter a number: "))
fibonacci(num)