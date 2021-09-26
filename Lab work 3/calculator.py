import statistics
input_nums = list()
while True:
    numbers = input()
    if numbers == "":
        break
    numbers = int(numbers)
    input_nums.append(numbers)
lenth = len(input_nums)
for i in range(lenth):
    for j in range(0, lenth - i -1):
        if int(input_nums[j]) > int(input_nums[j + 1]):
            input_nums[j], input_nums[j + 1] = input_nums[j + 1], input_nums[j]
sum_of_nums = 0
for i in input_nums:
    sum_of_nums = sum_of_nums + int(i)
mean = 0
for i in input_nums:
    mean += int(i)
end_mean = mean / lenth
mode = statistics.multimode(input_nums)

print("minimum =", input_nums[0])
print("maximum =", input_nums[lenth - 1])
print("range =", input_nums)
print("count =", lenth)
print("sum =", sum_of_nums)
print("mean =", end_mean)
print("mode =", mode[0])