def total_occurrences(s1, s2, ch):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Returns sum of ch's occurrences in s1 and s2.
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    final_line = s1 + s2
    occurrences_in_final_line = final_line.count(ch)
    return int(occurrences_in_final_line)
