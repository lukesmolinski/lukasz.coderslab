n = int(input("Enter a number from 1 to 10: "))

while n < 1 or n > 10:
    print("Number is out of range!")
    n = int(input("Enter a number from 1 to 10: "))

for i in range(1, 11):
    result = n * i
    print(n, "x", i, "=", result)

    