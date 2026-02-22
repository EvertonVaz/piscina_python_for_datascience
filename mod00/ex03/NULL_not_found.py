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
