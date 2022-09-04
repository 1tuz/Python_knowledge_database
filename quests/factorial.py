def factorial_func():
    n = int(input("Enter your value : "))

    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1

    print(f"Factorial of the value is : {factorial}")


factorial_func()
