family = [
    {"first_name": "Caren", "last_name": "Khachatrian", "birth_year": 1977},
    {"first_name": "Hripsime", "last_name": "Shirvanian", "birth_year": 1979},
    {"first_name": "Gregory", "last_name": "Khachatrian", "birth_year": 2013},
    {"first_name": "Anais", "last_name": "Khachatrian", "birth_year": 2015}
]

# MIXED List
family_list = []
for member in family:
    family_list.append([member["first_name"], member["last_name"], member["birth_year"]])

# EXTEND List
new_member = ['Anabelle']
new_member.extend(['Kitty', 2022])
family_list.append(new_member)

another_member = ['Mko']
another_member += ['Xamyak', 2025]
family_list.append(another_member)

# SPLICE Insert
last_member = ['Tatev']
last_member.append(2026)
last_member[1:1] = ['Moghess']
family_list.append(last_member)

print(family_list)

# SET
last_names = set()
for person in family:
    last_names.add(person["last_name"])

my_extended_family_last_names = {"Khachatrian", "Ptoukyan"}

print(last_names)
# {'Khachatrian', 'Shirvanian'}

# INTERSECT
intersect = last_names & my_extended_family_last_names
print(intersect)

# UNION
union = last_names | my_extended_family_last_names
print(union)

# DIFFERENCE
diff = last_names - my_extended_family_last_names
print(diff)

# SUBSET
subset = last_names < union
print(subset)

# SUPERSET
superset = union > last_names
print(superset)

# SET Comprehensions
test_set = {member["first_name"] for member in family}
print(test_set)