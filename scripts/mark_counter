counter_triple_plus = -2
counter_double_plus = -2
counter_minus = -2

with open("path", "r", encoding="utf-8") as file:
    for line in file:
        if "**+++**" in line:
            counter_triple_plus += 1

        if "**++**" in line:
            counter_double_plus += 1

        if "**—**" in line:
            counter_minus += 1
print(counter_triple_plus)
print(counter_double_plus)
print(counter_minus)
print(counter_triple_plus + counter_double_plus + counter_minus)
