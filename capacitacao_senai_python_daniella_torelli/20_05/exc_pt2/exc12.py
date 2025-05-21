numbers = [12, 67, 89, 23, 51, 76, 5, 94, 8, 60]

numbers_above50 = []

for i, n in enumerate(numbers):
    if n > 50:
        numbers_above50.append(n)

print(numbers_above50)
