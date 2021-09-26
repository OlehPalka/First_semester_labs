x = int(input())
a = 0 
result = 5**x
bin_result = bin(result)
bin_result = bin_result[2:]
for i in bin_result:
    a += int(i)
if a % 2 == 0:
    print("Number {} is evil number. Its hamming weight is {}.".format(result, a))
else:
    print("Number {} is odious number. Its hamming weight is {}.".format(result, a))
