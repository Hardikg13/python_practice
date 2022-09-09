def factorial(number):
    factorial = 1
    if number < 0:
        print("Factorial of negative numbers do not exist")
    elif number == 1:
        print(1)
    else:
        for i in range(1, number + 1):
            factorial = factorial * i
        return factorial


if __name__ == '__main__':
    print("Enter a Number:")
    number = int(input())
    print("The factorial of", number, "is", factorial(number))
