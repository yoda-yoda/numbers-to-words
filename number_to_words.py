"""Convert Numbers to Words.

1001 - One thousand and One
"""
import math


class NumbersToWord(object):
    """Convert Numbers to words."""

    hyphen = '-'
    conjunction = ' and '
    separator = ', '
    negative = 'negative '
    decimal = ' point '
    space = ' '

    dictionary = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'fourty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
        1000000: 'million',
        1000000000: 'billion',
        1000000000000: 'trillion',
        1000000000000000: 'quadrillion',
        1000000000000000000: 'quintillion'
    }

    def number_to_words(self, number):
        """Convert a number into words."""
        if not isinstance(number, (int, float,)):
            return False

        if number < 0:
            return self.negative + self.number_to_words(abs(number))

        string = fraction = None

        if "." in str(number):
            number, fraction = str(number).split('.')
        number = int(number)
        fraction = int(fraction) if fraction else fraction

        if number < 21:
            string = self.dictionary[number]

        elif number < 100:
            tens = (number / 10) * 10
            units = number % 10
            string = self.dictionary[tens]
            if units:
                string += self.hyphen + self.dictionary[units]

        elif number < 1000:
            hundreds = number / 100
            remainder = number % 100
            string = self.dictionary[hundreds] + self.space + \
                self.dictionary[100]
            if remainder:
                string += self.conjunction + self.number_to_words(remainder)
        else:
            log = math.floor(math.log(number, 1000))
            base_unit = math.pow(1000, log)
            num_base_units = int(number / base_unit)
            remainder = number % base_unit
            string = self.number_to_words(num_base_units) + self.space + \
                self.dictionary[base_unit]

            if remainder:
                string += self.conjunction if remainder < 100 else \
                    self.separator
                string += self.number_to_words(remainder)

        if (fraction is not None) and isinstance(fraction, int):
            string += self.decimal
            words = ''
            for each in str(fraction):
                words += self.dictionary[int(each)] + self.space
            string += words

        return string
