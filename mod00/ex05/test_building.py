from building import Building


def test_building():
    """
    This program, which takes a single string argument
    and displays the sums of its
    upper-case characters, lower-case
    characters, punctuation characters, digits and spaces.
    •If None or nothing is provided, the user is prompted to provide a string.
    •If more than one argument is provided to the program,
    print an AssertionError
    """

    # arrange
    input = """
Python 3.0, released in 2008, was a major revision that is not completely
backward-compatible with earlier versions.
Python 2 was discontinued with version 2.7.18 in 2020.
    """.strip()

    expected_length = 171
    expected_upper_length = 2
    expected_lower_length = 121
    expected_punctuation_length = 8
    expected_space_length = 25
    expected_digit_length = 15

    # act
    building = Building(input)
    building.building()
    actual_length = building.length
    actual_upper_length = building.upper_length
    actual_lower_length = building.lower_length
    actual_punctuation_length = building.punctuation_length
    actual_space_length = building.space_length
    actual_digit_length = building.digit_length

    # assert
    assert actual_length == expected_length
    assert actual_upper_length == expected_upper_length
    assert actual_lower_length == expected_lower_length
    assert actual_punctuation_length == expected_punctuation_length
    assert actual_space_length == expected_space_length
    assert actual_digit_length == expected_digit_length

def test_building_empty():
    # arrange
    input = ""
    expected_length = 0
    expected_upper_length = 0
    expected_lower_length = 0
    expected_punctuation_length = 0
    expected_space_length = 0
    expected_digit_length = 0

    # act
    building = Building(input)
    building.building()
    actual_length = building.length
    actual_upper_length = building.upper_length
    actual_lower_length = building.lower_length
    actual_punctuation_length = building.punctuation_length
    actual_space_length = building.space_length
    actual_digit_length = building.digit_length

    # assert
    assert actual_length == expected_length
    assert actual_upper_length == expected_upper_length
    assert actual_lower_length == expected_lower_length
    assert actual_punctuation_length == expected_punctuation_length
    assert actual_space_length == expected_space_length
    assert actual_digit_length == expected_digit_length

def test_building_assertion_error():
    import sys
    from io import StringIO
    from contextlib import redirect_stderr

    # arrange
    test_args = ["program_name", "arg1", "arg2"]

    # act
    original_argv = sys.argv
    sys.argv = test_args
    stderr = StringIO()
    with redirect_stderr(stderr):
        try:
            from building import main
            main()
        except AssertionError as e:
            error_message = str(e)
    sys.argv = original_argv

    # assert
    assert error_message == "Please provide a single string argument."