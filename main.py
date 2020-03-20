import re

f = open("Input/1.txt", "r")
f1 = f.readline()


def format_text(line):
    return re.sub(r'(\w+)\s+=\s+\1\s\+\s+1', r'\1++', line)


f = open("Output/1.txt", "w+")
f.write(format_text(f1))
