x, y = input().split( )
x = int(x)
y = int(y)

a = 0
A = bin(x ^ y)[2:]

for i in A:
    a += int(i)
print(a)




   

