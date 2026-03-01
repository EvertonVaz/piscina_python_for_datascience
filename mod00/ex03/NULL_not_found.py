def NULL_not_found(object: any) -> int:
    try:
        tp = type(object)
        if object is None:
            print(f"Nothing: {object} {tp}")
        elif tp is float:
            print(f"Cheese: {object} {tp}")
        elif tp is int:
            print(f"Zero: {object} {tp}")
        elif tp is str and object == "":
            print(f"Empty: {object} {tp}")
        elif tp is bool and not object:
            print(f"Fake: {object} {tp}")
        else:
            raise TypeError("Type not Found")
        return 0
    except TypeError as e:
        print(e)
        return 1


if __name__ == "__main__":
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))
