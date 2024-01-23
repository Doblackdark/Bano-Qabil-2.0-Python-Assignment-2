print("Calculate the factoral of Value")
n = int(input("Enter any number: "))

f = 1

for i in range(n, 0, -1):
    f *= i

print("Factorial is", f)