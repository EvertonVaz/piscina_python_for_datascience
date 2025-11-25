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

        return (
            self.length,
            self.upper_length,
            self.lower_length,
            self.punctuation_length,
            self.digit_length,
            self.space_length,
        )


def main():
    if len(argv) != 2:
        raise AssertionError("Please provide a single string argument.")

    input_string = argv[1]
    b = Building(input_string)
    b.building()

    print(f"The text contains {b.length} characters:")
    print(f"{b.upper_length} upper letters")
    print(f"{b.lower_length} lower letters")
    print(f"{b.punctuation_length} punctuation marks")
    print(f"{b.space_length} space")
    print(f"{b.digit_length} digit")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")