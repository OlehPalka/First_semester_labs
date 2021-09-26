def caesar_decode(message, key):
    """
    (str, int) -> str
    This function decodes caesar code using key and massage.

    >>> caesar_decode("ifmmp xpsme", 1)
    'hello world'
    >>> caesar_decode("jg zpv ibqqz boe zpv lopx ju dmbq zpvs iboe", 1)
    'if you happy and you know it clap your hand'
    """
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    decode_centence = list()
    for i in message:
        if i == " ":
            decode_letter = i
        else:
            x = alfabet.find(i)
            decode_letter = alfabet[(x - key) % 26]
        decode_centence.append(decode_letter)
    result = "".join(decode_centence)
    return result
print(caesar_decode("ifmmp xpsme", 1))
def caesar_encode(message, key):
    """
    (str, int) -> str
    This function encodes message to caesar code using key.
    >>> caesar_encode("hello world", 1)
    'ifmmp xpsme'
    >>> caesar_encode("if you happy and you know it clap your hand", 1)
    'jg zpv ibqqz boe zpv lopx ju dmbq zpvs iboe'
    """
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    code_centence = list("")
    for i in message:
        if i == " ":
            code_letter = i
        else:
            x = alfabet.find(i)
            code_letter = alfabet[(x + key) % 26]
        code_centence.append(code_letter)
    result = "".join(code_centence)
    return str(result)

print(caesar_encode("if you happy and you know it clap your hand", 1))