ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Brasil")
ft_set.remove("tutu!")
ft_set.update({"Hello", "São Paulo!"})
ft_dict["Hello"] = "42sp"

def tests():
    try:
        assert ft_list == ["Hello", "World!"], f"Expected ['Hello', 'World!'], got {ft_list}"
        assert ft_tuple == ("Hello", "Brasil"), f"Expected ('Hello', 'Brasil'), got {ft_tuple}"
        assert ft_set == {"Hello", "São Paulo!"}, f"Expected {{'Hello', 'São Paulo!'}}, got {ft_set}"
        assert ft_dict == {"Hello": "42sp"}, f"Expected {{'Hello': '42sp'}}, got {ft_dict}"
        print("\033[32mTests passed successfully!\033[0m\n")
    except AssertionError as e:
        print("Error: Test failed", e)
        return e

tests()

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)