f = open("Input/1.txt", "r")
f1 = f.readlines()


def reverse_text(lines):
    res = []
    for i in lines:
        resLine = []
        line = i.split()
        for j in line:
            resLine.append(j[::-1])
            resLine.append(" ")
        res.append(resLine)
    return str(res)


print(reverse_text(f1))
