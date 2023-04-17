numbers = []

n = int(input("Enter n: "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

sum_numbers = sum(numbers)
avg_numbers = sum_numbers / n

print("Entered numbers:", " ".join(str(x) for x in numbers))
print("Sum:", sum_numbers)
print("Average:", avg_numbers)

if sum_numbers > avg_numbers:
    print("The sum is greater!")
else:
    print("The sum is not greater!")