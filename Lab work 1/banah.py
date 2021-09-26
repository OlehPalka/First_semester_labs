import random
num_trials = 100
booklet_size = 40
matches = {}

for i in range(num_trials):
    booklet1 = booklet2 = booklet_size
    while booklet1 > 0 and booklet2 > 0:
        r = random.random()
        if r < 0.5:
            booklet1 -= 1
        else:
            booklet2 -= 1
    mtch = booklet1 + booklet2
    if mtch in matches:
        matches[mtch] += 1
    else:
        matches[mtch] = 1      

print(sorted(list(matches.items())))
for key in matches:
    print(key, matches[key]/num_trials)