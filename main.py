import re

f = open("Input/text.txt", "r")
f1 = f.readlines()
f2 = open("Input/1.txt", "r")
keys = f2.readlines()


def format_text(key, l):
    return re.findall(rf'\s+{key}\s+', l)


f = open("Output/1.txt", "w+")
for line in keys:
    for key in line.split():
        for l in f1:
            f.write(', '.join(re.findall(rf'\s+{key}\s+', l)))
