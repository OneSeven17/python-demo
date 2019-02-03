def cashback(monthly_expenses): # объявление функции
    """

    >>> cashback(10_000)
    300.0
    """
# здесь не должно быть функции print иначе доктест не будет проходить корректно
    percent = 3 # отступ(табуляция) внутри функции обязателен
    result = percent * monthly_expenses / 100
    return result # возврат значения - результат который выдает функция

def bmi(weight, length):
    """
    >>> bmi (106, 1.68) # doctest: +ELLIPSIS
    37.55...
    """
    result = weight / length ** 2
    return result