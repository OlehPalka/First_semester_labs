def create_acronym(sentence):
    r"""
    str -> str
    This function returns acronym from input sentence.
    It rturns acronym even from words started with small letter.

    >>> create_acronym('random access memory\nAs soon As possible')
    'RAM - random access memory\nASAP - As soon As possible'
    >>> create_acronym("Факультет прикладних наук\nУкраїнський Католицький Університет")
    'ФПН - Факультет прикладних наук\nУКУ - Український Католицький Університет'
    >>> create_acronym("Основи Програмування\nДискретна Математика\nMath analysis\nComputer science\nBusiness analysis")
    'ОП - Основи Програмування\nДМ - Дискретна Математика\nMA - Math analysis\nCS - Computer science\nBA - Business analysis'
    """

    splited_senteces = sentence.split("\n")
    finalresult = list("")
    for m in range(len(splited_senteces)):
        BIG_letters = list()
        end_sentence = splited_senteces[m]
        cap_sentence = splited_senteces[m].title()
        cap_sentence = cap_sentence.split(" ")
        for i in range(len(cap_sentence)):
            x = cap_sentence[i]
            while True:
                try:
                    x = x.replace(x[1], "")
                    if len(x) == 1:
                        break
                except IndexError:
                    x = x[0]
                    break
            BIG_letters.append(x)
        result = "\n" + ''.join(BIG_letters) + " - " + ''.join(end_sentence)
        finalresult.append(result)
    finalresult = "".join(finalresult)
    return finalresult[1:]

print(create_acronym('random access memory\nAs soon As possible'))