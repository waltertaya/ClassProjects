n = 7
i = 4

objects = ["A", "B", "C", "D", "E", "F", "G", "H"]
combinations = []


def combination(n, i):
    for j in range(n):
        if i == 1:
            yield [objects[j]]
        else:
            for next in combination(j + 1, i - 1):
                yield [objects[j]] + next


for c in combination(n, i):
    combinations.append(c)

print(combinations)
print(len(combinations))
