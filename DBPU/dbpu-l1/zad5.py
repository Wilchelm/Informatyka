from pathlib import Path

path = input("Enter file path: ")
word = input("Enter word to search in file: ")

my_file = Path(path)
if my_file.is_file():
    with open(path) as f:
        for line in f:
            if word in line:
                print (line)
else:
    print ("File not exist.\n")
