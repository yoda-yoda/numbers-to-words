"""Convert Numbers to Words.

1001 - One thousand and One
"""
import math

from wordsapp.base_wrapper import NumbersBaseWrapper


class NumbersToWord(NumbersBaseWrapper):
    """Convert Numbers to words."""

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
