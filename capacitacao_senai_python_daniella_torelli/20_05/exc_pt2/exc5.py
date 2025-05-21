names = ['matheus', 'camila', 'alberto', 'marcia', '']

emails = []

for i, name in enumerate(names):
    names_string = '@gmail.com '.join(names)
    names_array = names_string.split(' ')
print(names_array)

for i in range(len(names_array)):
        emails.append(names_array[i])

print(' - '.join(emails))
