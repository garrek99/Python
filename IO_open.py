names = []

for _ in range[3]:
    names.append(input("What's your name? "))

with open("names.txt", "a") as file:
    for name in sorted(names):
        file.writelines(f"hello, {name}")

with open("names.txt", "r") as file2:
    #linesList = file2.readlines()
    for line in file2:
        print("hello,", line.rstrip())

