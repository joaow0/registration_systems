# People registration system using dictionaries and lists
record = {}
people = []
age_sum = 0

while True:
    record['name'] = input('Name: ').strip()

    record['gender'] = input('Gender: [M/F] ').strip()
    while record['gender'] not in 'MmFf':
        record['gender'] = input('Invalid gender, please try again: ').strip()

    record['age'] = int(input('Age: '))
    while record['age'] < 0 or record['age'] > 100:
        record['age'] = int(input('Invalid age, please try again: '))

    age_sum += record['age']
    people.append(record.copy())  # Store a copy of the current dictionary in the list

    continue_input = input('Do you want to continue? [Y/N] ').strip()
    if continue_input in 'Nn':
        break

# Average age calculation
average = age_sum / len(people)

print(f'\n{len(people)} people were registered.')
print(f'The average age of the group is {average:.1f} years.')

# List of registered women
print('Registered women:', end=' ')
for p in people:
    if p['gender'] in 'Ff':
        print(p['name'], end='. ')
print()

# People above average age
above_average = [p for p in people if p['age'] > average]
if not above_average:
    print('No one is above the average age.')
else:
    print('People above the average age:', end=' ')
    for p in above_average:
        print(f"{p['name']} ({p['age']} years)", end='. ')