persons = [
    {"name": "Po","age": 30},
    {"name": "Ro","age": 27}
]

#Lambda function is used here
persons.sort(key=lambda item: item['name'])
print(persons)