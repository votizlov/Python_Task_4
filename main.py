import re

f = open("Input/text.txt", "r")
f1 = f.readline()
f2 = open("Input/1.txt", "r")
keys = f2.readlines()


def format_text(key):
    return re.findall(rf'\s+{key}\s+', f1)


f = open("Output/1.txt", "w+")
for line in keys:
    for key in line.split():
        print(re.findall(rf'\s+{key}\s+', f1))
        f.write(', '.join(re.findall(rf'\s+{key}\s+', f1)))
