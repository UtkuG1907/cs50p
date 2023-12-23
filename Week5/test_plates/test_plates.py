from plates import is_valid


# “All vanity plates must start with at least two letters.”
def test_starting_two():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_length():
    assert is_valid("C") == False
    assert is_valid("COMPUTERSCIENCE50") == False


# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
def test_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


# “No periods, spaces, or punctuation marks are allowed.”
def test_punctuation():
    assert is_valid("HELLO!") == False
    assert is_valid("CS50.") == False
