import textwrap

f = open("Input/text.txt", "r")
f1 = f.readlines()
f2 = open("Input/1.txt", "r")
keys = f2.readlines()

textWith = 10

f = open("Output/1.txt", "w+")
for l in f1:
    f.write("\n" + "      " + textwrap.fill(l,textWith))
