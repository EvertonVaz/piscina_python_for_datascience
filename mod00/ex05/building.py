from sys import argv


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

    def __init__(self, input_string: str):
        self.input_string = input_string
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
            if char.isupper():
                self.upper_length += 1
            elif char.islower():
                self.lower_length += 1
            elif char.isdigit():
                self.digit_length += 1
            elif char.isspace():
                self.space_length += 1
            elif not char.isalnum():
                self.punctuation_length += 1

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
    if len(argv) > 2:
        raise AssertionError("Please provide a single string argument.")

    if len(argv) == 1:
        argv.append(" " + input("What is the text to count?\n"))

    input_string = argv[1]

    print(Building(input_string))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
