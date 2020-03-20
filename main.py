import re

f = open("Input/1.txt", "r")
f1 = f.readline()


def format_text(line):
    return str(re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b',f1))


f = open("Output/1.txt", "w+")
print(re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b',f1))
f.write(format_text(f1))
