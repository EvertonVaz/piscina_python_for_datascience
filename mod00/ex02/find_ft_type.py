def all_thing_is_obj(object: any) -> int:
    tp = type(object)

    if tp.__name__ == "int":
        print("Type not found")
    elif tp.__name__ == "str":
        print(f"{object} is in the kitchen : {tp}")
    else:
        print(f"{tp.__name__.capitalize()} : {tp}")

    return 42


if __name__ == "__main__":
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}
    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    all_thing_is_obj("Toto")
    print(all_thing_is_obj(10))