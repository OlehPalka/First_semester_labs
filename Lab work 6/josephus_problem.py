def josephus(ls, skip):
    skip -= 1 #pop automatically skips the dead guy
    idx = skip
    while len(ls) > 1:
        print(ls.pop(idx), ls)
        idx = (idx + skip) % len(ls)
    print("survivor ", ls[0])

josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15], 3)