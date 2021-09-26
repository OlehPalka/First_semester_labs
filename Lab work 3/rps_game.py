S_P_R = list()
while True:
    combination = input()
    if combination == "":
        break
    S_P_R.append(combination)
for i in S_P_R:
    if i == "SS" or i == "PP" or i == "RR":
        print("False | False")
    elif i == "SP" or i == "PR" or i == "RS":
        print("True")
    else:
        print("False")