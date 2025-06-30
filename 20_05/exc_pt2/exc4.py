numbers = [10, -23, 17.4, 0, -3.14, -45, 123, -97.345, 100, 200, 300, -1.1, -0.001, -89, 56]

for i, n in enumerate(numbers):
    if n < 0: 
        numbers[i] = 0

print(numbers)
