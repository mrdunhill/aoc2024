import os

num = os.path.basename(__file__).split(".")[0]
with open(f"{num}.txt") as f:
    lines = f.readlines()

# Make sorted lists from each column
lcol = []
rcol = []
for line in lines:
    a, b = line.strip().split()
    lcol.append(int(a))
    rcol.append(int(b))
lcol = sorted(lcol)
rcol = sorted(rcol)

# Part 1
result_1 = 0
for a, b in zip(lcol, rcol):
    result_1 += abs(a - b)
print(f"Part 1: {result_1}")

# Part 2
result_2 = 0
for value in lcol:
    result_2 += value * rcol.count(value)
print(f"Part 2: {result_2}")