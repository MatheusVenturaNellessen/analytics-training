# exc1
array = [10, 'Matheus', True, -12.5]
print(array)

# exc2
array.append(False)
print(len(array))

# exc3
new_array = [100, 200, 300]
array.extend(new_array)
print(array)

# exc4
array.insert((int(len(array)/2)), 'meio')
print(array)

# exc5
array.remove(100)
# array.remove(999) # ValueError: list.remove(x): x not in list
print(array)

# exc6
print(array.pop(3))

# exc7
array.clear()
print(array)

# exc8
fruits = ['maça', 'banana', 'laranja', 'banana']
print(fruits.index('banana'))

# exc9
counter = fruits.count('banana')
print(counter)

# exc10
fruits_reverse = fruits.reverse()
print(fruits_reverse) # Está com um bug!

# exc11
string = 'python, java, c++'
print(string.split(','))

# exc12
languages = ['py', 'js', 'rb']
print(' - '.join(languages))

# exc13
print(' Hello World '.strip())

# exc14
print(' apple;banana;cherry '.strip().split(';'))

#exc15
numbers = [1, 2, 3, 4 , 5]
while len(numbers) != 0:
    print(numbers)
    numbers.pop()

print(numbers)

# exc16
names_array = 'Matheus Camila Ecoli Pierre'.split(' ')
print(names_array)
names_array.reverse()
print(names_array)
names_string = '-'.join(names_array)
print(names_string)
