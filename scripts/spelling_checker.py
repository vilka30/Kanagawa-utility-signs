path = "path"
a = False
poles = []

with open(path, "r", encoding="utf-8") as file:
    for line in file:
        if "**На верхней:**" in line:
            a = True
        if line.startswith('- ') and a == True:
                    poles.append(line.split("- ")[1].strip())
        if line.strip() == '':
                    a = False

for i in poles:
    if '支' not in i and '幹' not in i and '分'not in i:
        print(i)
