def calculate_expression(expression):
    """


    >>> calculate_expression("Скільки буде 2 плюс 2?")
    4
    >>> calculate_expression("Скільки буде 2 додати 2 поділити на 2?")
    2
    >>> calculate_expression("Скільки буде 3?")
    3
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    >>> calculate_expression("Скільки буде 2 2 додати?")
    'Неправильний вираз!'
    """
    #"додати"/"плюс", "відняти"/"мінус", "помножити на", "поділити на"
    expression = expression.replace("додати", "+")
    expression = expression.replace("плюс", "+")
    expression = expression.replace("відняти", "-")
    expression = expression.replace("мінус", "-")
    expression = expression.replace("помножити на", "*")
    expression = expression.replace("поділити на", "//")
    expression = expression.replace("Скільки буде ", "")
    expression = expression.replace("?", "")
    expression = list(expression.split (" "))
    if len(expression) == 1:
        x = eval(expression[0])
        return x
    if len(expression) == 2:
        x = "Неправильний вираз!"
        return x
    needed_expressions = [expression[0], expression[1], expression[2]]
    calculated_expression = ' '.join(needed_expressions)

    try:
        x = eval(calculated_expression)
    except (ZeroDivisionError, SyntaxError):
        x = "Неправильний вираз!"
        y = x
        return y
    n = 3
    x = str(x)
    while True:
        if n == len(expression):
            break
        needed_expressions = [x, expression[n], expression[n + 1]]
        calculated_expression = ' '.join(needed_expressions)
        x = eval(calculated_expression)
        x = str(x)
        n += 2
    return int(x)
