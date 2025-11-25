from sys import argv
from typing import List


class Building:
    """
    This class takes a single string argument and calculates the sums of its
    upper-case characters,
    lower-case characters,
    punctuation characters,
    digits and spaces.
    """

    length = 0
    upper_length = 0
    lower_length = 0
    punctuation_length = 0
    digit_length = 0
    space_length = 0

    def __init__(self, input_string: List[str]):
        if len(input_string) > 2:
            raise AssertionError("Please provide a single string argument.")

        self.input_string = input_string[1]
        self.building()

    def building(self):
        """
        This method calculates the sums of upper-case characters,
        lower-case characters,
        punctuation characters,
        digits and spaces in the input string.
        """
        self.length = len(self.input_string)
        for char in self.input_string:
            self.upper_length += char.isupper()
            self.lower_length += char.islower()
            self.digit_length += char.isdigit()
            self.space_length += char.isspace()
            self.punctuation_length += (not char.isalnum() and not char.isspace())

    def __str__(self):
        return (
            f"The text contains {self.length} characters:\n"
            f"{self.upper_length} upper letters\n"
            f"{self.lower_length} lower letters\n"
            f"{self.punctuation_length} punctuation marks\n"
            f"{self.space_length} space\n"
            f"{self.digit_length} digit"
        )


def main():
    if len(argv) == 1:
        argv.append(" " + input("What is the text to count?\n"))

    print(Building(argv))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
