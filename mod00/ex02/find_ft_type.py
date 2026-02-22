def all_thing_is_obj(object: any) -> int:
    tp = type(object)

    if tp.__name__ == "int":
        print("Type not found")
    elif tp.__name__ == "str":
        print(f"{object} is in the kitchen : {tp}")
    else:
        print(f"{tp.__name__.capitalize()} : {tp}")

    return 42
