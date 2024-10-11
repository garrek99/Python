import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["Name"], "house": row["House"]})
    """reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})"""
    """for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})"""

def get_house(student):
    return student["house"]

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")

