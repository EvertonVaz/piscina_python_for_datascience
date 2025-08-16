import sys

def what_is():
    if len(sys.argv) < 2:
        return
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        arg = int(sys.argv[1])

        if arg % 2 == 0:
            return(print("I'am Even"))
        return(print("I'am Odd"))

    except Exception:
        print("AssertionError: argument is not an integer")

what_is()