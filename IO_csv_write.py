import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("data\\names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Home"])
    writer.writerow({"Name" : name, "Home": home})