path = "path"
poles_strings_upper = []
poles_strings_under = []

duplicates_upper = []
duplicates_under = []

a = ""

def line_splitter(line):
    done_line = line.split("- ")[1].strip()
    return done_line

with open(path, "r", encoding="utf-8") as file:
    for line in file:
        if "**На нижней:**" in line:
            a = "under"
        elif "**На верхней:**" in line:
            a = "upper"

        if line.startswith("- "):
            if a == "under":
                poles_strings_under.append(line_splitter(line))
            elif a == "upper":
                poles_strings_upper.append(line_splitter(line))

seen_under = set()
seen_upper = set()

for i in poles_strings_under:
    if i not in seen_under:
        seen_under.add(i)
    else:
        duplicates_under.append(i)

for i in poles_strings_upper:
    if i not in seen_upper:
        seen_upper.add(i)
    else:
        duplicates_upper.append(i)


with open(path, "r", encoding="utf-8") as file:
    for line in file:
            if "**На нижней:**" in line:
                a = "under"
            elif "**На верхней:**" in line:
                a = "upper"

            if line.startswith('- '):
                if line_splitter(line) in duplicates_under and "**~**" not in line and a == "under":
                    print(line)
                if line_splitter(line) in duplicates_upper and "**~**" not in line and a == "upper":
                    print(line)
