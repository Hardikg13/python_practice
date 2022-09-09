print("Enter a Number: ")
number = int(input())
temp = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if temp == reverse:
    print("Number is a Palindrome")
else:
    print("Number is not a Palindrome")
