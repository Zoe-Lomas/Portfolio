def number_to_english(n: int) -> str:
    """ Translate an integer into words form

    :param n: the integer to translate
    :return: the English phrasing of :math:`n`

    >>> number_to_english(127)
    'one hundred and twenty-seven'
    """

    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n <= 90 and n % 10 == 0:
        return tens[n // 10]
    elif 20 < n < 100:
        return tens[n // 10] + ones[n % 10]
    elif 100 <= n <= 900 and n % 100 == 0:
        return ones[n // 100] + "hundred"
    elif 100 < n < 1000:
        return ones[n // 100] + "hundredand" + number_to_english(n % 100)
    elif 1000 < n < 10000:
        pass
    elif n == 1000:
        return "onethousand"
    else:
        raise ValueError("unexpected input")

letters = 0
for i in range(1,1001):
    name = number_to_english(i)
    a = len(name)
    letters += a
    print(name," ",a," ",letters)

print(number_to_english(127))
