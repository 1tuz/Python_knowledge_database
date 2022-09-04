def fib_func():
    fib1 = fib2 = 1
    n = int(input("Enter the value : "))
    print("The Fibonacci is :")
    print(fib1, fib2, ' ')

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, ' ')


fib_func()
