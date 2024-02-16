#!/usr/bin/python3
"""A module containing text_indentation function."""


def text_indentation(text):
    """Prints a text with new lines after each of these
    characters: '.','?' and ':'.
    Args:
        text (str) : String to print.
    Raises:
        TypeError: if text not a string.

    >>> text_indentation("String")
    String
    >>> text_indentation(56)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    is_whitespace = False
    # end_of_line = False
    for s in text:
        if s in ('.', '?', ':'):
            print(s)
            print()
            is_whitespace = True
            # end_of_line = True
        elif s.isspace():
            if is_whitespace:
                #end_of_line = False
                pass
            elif is_whitespace:
                print(s, end="")
            else:
                print(s, end="")
        else:
            print(s, end="")
            is_whitespace = False


if __name__ == "__main__":
    doctest.testfile('tests/5-text_indentation.txt')
