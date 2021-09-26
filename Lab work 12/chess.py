
def chess_puzzle(offi, queen):
    alfabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
    chess_greed = {alfabet[letter] + str(num)
                   for letter in range(8) for num in range(8)}
    officer = set()
    officer.add(offi)
    try:
        index_offi = alfabet.index(offi[0])
    except ValueError:
        return -1
    num_offi = int(offi[1])
    while num_offi < 8 or index_offi <= 6:
        officer.add(alfabet[index_offi + 1] + str(num_offi + 1))
        num_offi += 1
        index_offi += 1
    num_offi = 8
    index_offi = alfabet.index(offi[0])
    while num_offi > 2 or index_offi >= 1:
        officer.add(alfabet[index_offi - 1] + str(num_offi - 1))
        num_offi -= 1
        index_offi -= 1
    num_offi = 8
    index_offi = alfabet.index(offi[0])
    while num_offi > 2 or index_offi < 7:
        officer.add(alfabet[index_offi + 1] + str(num_offi - 1))
        num_offi -= 1
        index_offi += 1
    while num_offi > 8 or index_offi < 7:
        officer.add(alfabet[index_offi + 1] + str(num_offi - 1))
        num_offi -= 1
        index_offi += 1
    return officer


print(chess_puzzle("b2", "g3"))
