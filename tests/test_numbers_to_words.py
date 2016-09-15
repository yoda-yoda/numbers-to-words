"""Test case suite for numbers to words app."""
import pytest

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

    def test_a_none_int_or_float_passed_to_the_number_method(self):
        """A Non convertible string to a number should raise a ValueError."""
        with pytest.raises(ValueError) as e:
            self.number_to_words('NaN')
        assert 'NaN' in str(e.value)

    def test_a_passing_a_string_form_of_a_number(self):
        """A convertible string to a number should succeed."""
        one_twenty = self.number_to_words('120')
        assert one_twenty == 'One Hundred And Twenty'

    def test_a_negative_number_as_a_string(self):
        """A convertible (negative)string to a number should succeed."""
        negative_one_twenty = self.number_to_words('-120')
        assert negative_one_twenty == 'Negative One Hundred And Twenty'

    def test_a_positive_number_as_a_string(self):
        """A convertible (positive)string to a number should succeed."""
        four_one_twenty = self.number_to_words('420')
        assert four_one_twenty == 'Four Hundred And Twenty'

    def test_a_four_digit_number_with_a_remainder(self):
        """Convert a four digit number with a remainder."""
        result = self.number_to_words(1243)
        msg = 'One Thousand, Two Hundred And Fourty-three Point Zero '
        assert result == msg

    def test_a_four_digit_number_without_a_remainder(self):
        """Convert a four digit number without a remainder."""
        result = self.number_to_words(2000)
        assert result == 'Two Thousand'

    def test_passing_a_number_to_the_title_case_method(self):
        """Raise an assetion error if a number is passed."""
        with pytest.raises(AssertionError) as e:
            self.title_case(2345)
        assert 'Ensure you pass a string.' == str(e.value)
