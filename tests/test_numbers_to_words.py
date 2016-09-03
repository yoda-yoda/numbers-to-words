"""Test case suite for numbers to words app."""
from wordsapp.number_to_words import NumbersToWord


class TestNumbersToWords(NumbersToWord):
    """Test case suite for numbers to words app."""

    def test_a_one_digit_number(self):
        """Test that `1` equals one."""
        zero = self.number_to_words(0)
        one = self.number_to_words(1)
        two = self.number_to_words(2)
        three = self.number_to_words(3)
        four = self.number_to_words(4)
        five = self.number_to_words(5)
        six = self.number_to_words(6)
        seven = self.number_to_words(7)

        assert zero == 'Zero'
        assert one == 'One'
        assert two == 'Two'
        assert three == 'Three'
        assert four == 'Four'
        assert five == 'Five'
        assert six == 'Six'
        assert seven == 'Seven'

    def test_a_two_digit_number(self):
        """Test `11` equals eleven."""
        ten = self.number_to_words(10)
        twelve = self.number_to_words(12)
        fifteen = self.number_to_words(15)
        nineteen = self.number_to_words(19)
        twenty = self.number_to_words(20)

        assert ten == 'Ten'
        assert twelve == 'Twelve'
        assert fifteen == 'Fifteen'
        assert nineteen == 'Nineteen'
        assert twenty == 'Twenty'

    def test_a_three_digit_number(self):
        """Test `120` equals one hundred and twenty."""
        one_twenty = self.number_to_words(120)
        one_seventy = self.number_to_words(170)
        two_hundred = self.number_to_words(200)

        assert one_twenty == 'One Hundred And Twenty'
        assert one_seventy == 'One Hundred And Seventy'
        assert two_hundred == 'Two Hundred'
