import re

email = input("What's your email? ").strip()
if re.search(r"^\w+(\.\w+)?@(\w+\.)*\w+\..{2,3}$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid") 

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), ?(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

url = input("URL? ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(username)

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_])", url, re.IGNORECASE):
    print(f"Username: ", matches.groups(1))

"""_RegEx Cheatsheet_
    re.IGNORECASE
    re.MULTILINE
    re.DOTALL   the dot (.) represents all characters including newline
    
    .       any character except newline
    *       0 or more repetitions
    +       1 or more repetitions
    ?       0 or 1 repetition
    {m}     m repetitions
    {m,n}   m-n repetitions
    ^       at the start of the string
    $       just before the newline at the end of the string
    []      set of characters
    [^]     complementing the set, aka EXCEPT
    \w      [a-zA-Z0-9_], aka WORD character
    \W      not a WORD character
    \d      decimal digit
    \D      not a decimal digit
    \s      whitespace characters
    \S      not whitespace characters
    A\B     either A or B
    (...)   a group
    (?:...) non-capturing version
"""