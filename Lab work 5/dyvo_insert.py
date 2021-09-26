def dyvo_insert(sentence, flag):
    """
    (str, str) -> str
    Inserting word "диво" before every word that starts with flag.

    >>> dyvo_insert('Кит китро ираолурооп киитан.', 'кит')
    'дивокит дивокитро ираолурооп киитан.'
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "кит")
    'дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    """
    sentence = sentence.lower()
    replasing_string = "диво" + flag
    new_sentence = sentence.replace(flag, replasing_string)
    return new_sentence
    