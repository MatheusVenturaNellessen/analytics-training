numbers = list(range(1, 50001))

counter = 0

for i, n in enumerate(numbers):
    if n % 2 == 0:
        counter += 1

print(counter)
