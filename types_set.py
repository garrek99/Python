family = [
    {"first_name": "Caren", "last_name": "Khachatrian"},
    {"first_name": "Hripsime", "last_name": "Shirvanian"},
    {"first_name": "Gregory", "last_name": "Khachatrian"},
    {"first_name": "Anais", "last_name": "Khachatrian"}    
]

last_names = set()

for person in family:
    last_names.add(person["last_name"])

print(last_names)