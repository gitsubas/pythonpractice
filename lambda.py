square = lambda x: x * x
# print(square(2))

people = [
    {"name": "Subas", "house": "dadhikot" },
    {"name": "Anjana", "house": "Pakali"},
    {"name": "tejasvi", "house": "dadhikot"}
]

people.sort(key = lambda person: person["name"])

print(people)