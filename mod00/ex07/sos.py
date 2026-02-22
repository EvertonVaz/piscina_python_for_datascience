import sys

NESTED_MORSE = {
    "A": {".-"},
    "B": {"-..."},
    "C": {"-.-."},
    "D": {"-.."},
    "E": {"."},
    "F": {"..-."},
    "G": {"--."},
    "H": {"...."},
    "I": {".."},
    "J": {".---"},
    "K": {"-.-"},
    "L": {".-.."},
    "M": {"--"},
    "N": {"-."},
    "O": {"---"},
    "P": {".--."},
    "Q": {"--.-"},
    "R": {".-."},
    "S": {"..."},
    "T": {"-"},
    "U": {"..-"},
    "V": {"...-"},
    "W": {".--"},
    "X": {"-..-"},
    "Y": {"-.--"},
    "Z": {"--.."},
    "1": {".----"},
    "2": {"..---"},
    "3": {"...--"},
    "4": {"....-"},
    "5": {"....."},
    "6": {"-...."},
    "7": {"--..."},
    "8": {"---.."},
    "9": {"----."},
    "0": {"-----"},
    " ": {"/"},
}


def main(ac: int, av: list[str]) -> None:
    if ac != 2:
        raise AssertionError("the arguments are bad")

    input = av[1]

    for char in input:
        if char.upper() not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")

    [print(" ".join(next(iter(NESTED_MORSE[char.upper()])) for char in input))]


if __name__ == "__main__":
    try:
        main(len(sys.argv), sys.argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")
