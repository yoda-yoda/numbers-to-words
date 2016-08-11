"""Convert Numbers to Words.

This package is mostly meant for financial purposes. Where you need to convert
some number into words.
For instance :
    1. (1001 - One thousand and One)
    2. (2032 - Two thousand and thirty two)
    3. (10,001 - Ten thousand and one)
"""
import math

from to_words.base_wrapper import NumbersBaseWrapper


class NumbersToWord(NumbersBaseWrapper):
    """Convert Numbers to words."""

    def to_words(self, number):
        """Convert a number into words."""
        if not isinstance(number, (int, float,)):
            return False

        if number < 0:
            return self.negative + self.to_words(abs(number))

        string = fraction = None

        if "." in str(number):
            number, fraction = str(number).split('.')
        number = int(number)
        fraction = int(fraction) if fraction else fraction

        if number < 21:
            string = self.dictionary[number]

        elif number < 100:
            # Get tens and ones
            tens = (number / 10) * 10
            units = number % 10
            string = self.dictionary[tens]
            if units:
                string += self.hyphen + self.dictionary[units]

        elif number < 1000:
            # Get hundreds and make a recursive call with the remainder
            hundreds = number / 100
            remainder = number % 100
            string = self.dictionary[hundreds] + self.space + \
                self.dictionary[100]
            if remainder:
                # Make a recursive call
                string += self.conjunction + self.to_words(remainder)
        else:
            # Make a recursive call for the num_base_units
            log = math.floor(math.log(number, 1000))
            base_unit = math.pow(1000, log)
            num_base_units = int(number / base_unit)
            remainder = number % base_unit
            string = self.to_words(num_base_units) + self.space + \
                self.dictionary[base_unit]

            if remainder:
                # Make a recurssive call for the remainder
                string += self.conjunction if remainder < 100 else \
                    self.separator
                string += self.to_words(remainder)

        if (fraction is not None) and isinstance(fraction, int):
            string += self.decimal
            words = ''
            for each in str(fraction):
                words += self.dictionary[int(each)] + self.space
            string += words

        return string
