def yell(*words):
    uppercased = map(str.upper, words)
    # List Comprehensions
    uppercased = [word.upper() for word in words]
    print(*uppercased)

yell("This", "is", "CS50")

family = [
    {"first_name": "Caren", "last_name": "Khachatrian"},
    {"first_name": "Hripsime", "last_name": "Shirvanian"},
    {"first_name": "Gregory", "last_name": "Khachatrian"},
    {"first_name": "Anais", "last_name": "Khachatrian"},
]

def is_khachatrian(m):
    return m["last_name"].lower() == "khachatrian"

#FILTER w/ FUNCTION
temp = filter(is_khachatrian, family)
#FILTER w/ LAMBDA
temp = filter(lambda p: p["last_name"].lower() == "khachatrian", family)

for person in sorted(temp, key=lambda p: p["first_name"]):
    yell(person["first_name"])

# ENUMERATE
print("Ordered by age:")
for i, member in enumerate(family, start=1):
    print(i, member["first_name"])

"""_reformat_file_
black .\map_filter.py
"""