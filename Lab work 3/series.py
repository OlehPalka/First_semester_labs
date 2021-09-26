n = int(input())
current_number = 0
for i in range(n):
    print(current_number + 1, "/", current_number + 2, sep= "", end = "")
    current_number += 2
    if n * 2 == current_number:
        break
    else:
        print(" - ", end = "")
        print(current_number + 1, "/", current_number + 2, sep= "", end = "")
        current_number += 2
        if n * 2 == current_number:
            break
        else:
            print(" + ", end = "")
print()
            