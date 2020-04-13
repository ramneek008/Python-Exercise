import keyword

keys = ["for", "while", "rajesh", "break", "land", "elif", "else", "go"]
for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is a python keyword")
    else:
        print(keys[i] + " is not a python keyword")