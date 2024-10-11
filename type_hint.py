def meow(n: int) -> str:
    return "Meow\n" * 3

number: int = input("Number: ")
meows: str = meow(number)
print(meows, end="")

#mypy .\type_hint.py