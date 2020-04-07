import re

f = open("Input/1.txt", "r")
f1 = f.readlines()
f = open("Input/text.txt","r")


def format_text(key):
    return re.findall(rf'\s+{key}\s+', f.readline())


f = open("Output/1.txt", "w+")
for line in f1:
    for key in line.split():
        print(key)
        f.write(str(format_text(key)))
