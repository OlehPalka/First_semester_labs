x = [2, 3, 4, 5, 6]
for i, _ in enumerate(x):
    x[i] = str(x[i])
print(" ".join(x))
