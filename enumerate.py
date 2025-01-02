x = [2000, 1000, -1, 5000, 3000, -1]
for index, value in enumerate(x):
    if value == -1:
        x[index] = 0
print(x)