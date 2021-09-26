def check_coincidence(dictionary_of_birthdays):
    ''' check_coincedence(dictionary_of_birthdays) -> bool
    Return information about coincedence in list(dictionary_of_birthdays)
      '''
    for key in dictionary_of_birthdays: 
        if dictionary_of_birthdays[key] >=2:
            return True
    return False

def count_probability(number_of_coincidence):
    '''count_probability(number_of_coincidence) -> number
    Retun probability of coincedence'''
    return number_of_coincidence/number_of_tries