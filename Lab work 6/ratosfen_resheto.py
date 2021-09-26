# from CMU 15-112
# http://www.cs.cmu.edu/~112
# Sieve of Eratosthenes
# This function returns a list of prime numbers
# up to n (inclusive), using the Sieve of Eratosthenes.
# See http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def  sieve_flavius(n): 
    lucky_num = 3
    list_of_nums = list()
    for i in range(n):
        if (i + 1) % 2 != 0:
            list_of_nums.append(i + 1)
    lucky_num_index = 1
    while True:
        del_index = 0            
        while True:
            compared_list = list_of_nums
            del_index += lucky_num - 1 
            if del_index > len(compared_list) - 1:
                break                    
            del list_of_nums[del_index]
        
        lucky_num_index += 1
        try:
            lucky_num = list_of_nums[lucky_num_index]
        except IndexError:
            break
    return list_of_nums
