"""
Sorts numbers
"""
def sieve_flavius(your_num: int) -> list:
    """
    This function completes sorting of numbers (n)
    by finding lucky numbers in the list.

    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    """
    lucky_num = 3
    list_of_nums = list()
    for i in range(your_num):
        #delet even numbers for first check
        if (i + 1) % 2 != 0:
            list_of_nums.append(i + 1)
    lucky_num_index = 1
    while True:
        del_index = 0
        # del_index - index for deleting numbers from list
        while True:
            compared_list = list_of_nums
            #creat new list for comarison if function is done
            del_index += lucky_num - 1
            if del_index > len(compared_list) - 1:
                break
            del list_of_nums[del_index]
            # encrease lucky number index
        lucky_num_index += 1
        try:
            lucky_num = list_of_nums[lucky_num_index]

        except IndexError:
            break
    return list_of_nums
