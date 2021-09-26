x = input()
n = 1
while True:
    bin_n = bin(n)[2:]
    y = "0" + bin_n
    lenth = len(bin_n)
    number = ""
    for i in range(lenth):
        number += str(int(y[i]) ^ int(bin_n[i]))
    if number == x:
        print(bin_n)
        break
    else:
        n += 1