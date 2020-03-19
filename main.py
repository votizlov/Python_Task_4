f = open("Input/1.txt", "r")
f1 = f.readlines()


def reverse_text(lines):
    res = ""
    for i in lines:
        resLine = ""
        line = i.split()
        for j in line:
            resLine += (j[::-1])
            resLine += " "
        res += resLine
        res += "\n"
    return str(res)


print(reverse_text(f1))
f = open("Output/1.txt", "w+")
f.write(reverse_text(f1))
