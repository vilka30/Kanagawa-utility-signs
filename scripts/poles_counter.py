path = "path"
poles_strings = []

with open(path, "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith('- '):
            poles_strings.append(line.split("- ")[1].strip())

setted_poles_strings = set(poles_strings)
print(f"Всего надписей: {len(poles_strings)}")
print(f"Всего уникальных надписей: {len(setted_poles_strings)}")
print(f"Всего повторов (Всего надписей - Всего уникальных надписей): {len(poles_strings) - len(setted_poles_strings)}")
