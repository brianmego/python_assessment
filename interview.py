#!/usr/bin/env python3
"""
Welcome to the python assessment!

Below you will find a series of unit tests. To complete the assessment,
replace the code on the commented out lines in each test function with your
own to make the tests pass.

To run this file, you can type ./interview.py if in a CLI, or
press the 'Run' button if in an online editor.

Good luck!
"""

def get_list_index(inp: list, index: int):
    """
    input:
        inp: [1, 2, 3]
        index: 2
    expected: 3
    """
    # Your code here to return the expected value


def uppercase_str(inp: str):
    """
    input:
        inp: 'hello world'
    expected: HELLO WORLD
    """
    # Your code here to return the expected value


def get_dict_value(inp: dict, key: str):
    """
    input:
        inp: {
            "spam": "eggs"
        }
        key: "spam"
    expected: "eggs"
    """
    # Your code here to return the expected value


def get_dict_value_with_default(inp: dict, key: str):
    """
    input:
        inp: {
            "spam": "eggs"
        }
        key: "foo"
    expected: "default"
    """
    # Your code here to return the expected value


def combine_lists(inp: list, inp2: list):
    """
    input:
        inp: [1, 2],
        inp2: [2, 3]
    expected: [1, 2, 2, 3]
    """
    # Your code here to return the expected value


def combine_lists_no_duplicates(inp: list, inp2: list):
    """
    input:
        inp: [1, 2],
        inp2: [2, 3]
    expected: [1, 2, 3]
    """
    # Your code here to return the expected value


def ensure_in_place(func):
    """Decorator for the next question. Nothing to see here"""

    def inner(inp, inc_value):
        _orig_id = id(inp)
        _orig = inp
        response = func(inp, inc_value)
        if id(response) != _orig_id:
            return 'Whoops! Looks like you made a new item in memory!'
        return response
    return inner


@ensure_in_place
def increment_in_place(inp: list, inc_value: int):
    """
    input:
        inp: [1, 2, 3]
        inc_value: 2
    expected: [3, 4, 5]
    """
    # Your code here to manipulate inp to the expected value
    return inp


def sum_list(inp: list):
    """
    input:
        inp: [1, 2, 3]
    expected==6
    """
    # Your code here to return the expected value


def left_pad(inp: str, total_length: int):
    """
    input:
        inp: 'hello'
        total_length: 10
    expected==00000hello
    """
    # Your code here to return the expected value


def flatten_dict(inp: dict):
    """
    input:
        inp: {
            "spam1": {
                "spam2": "eggs"
            },
            "eggs1": {
                "eggs2": "eggs3"
            },
        }
    expected=={
        "spam1": "spam2.spam3",
        "eggs1": "eggs2.eggs3"
        }
    """
    # Your code here to return the expected value


if __name__ == '__main__':
    challenge_list = [
        ('GetListIndex', get_list_index([1, 2, 3], 2), 3),
        ('UppercaseString', uppercase_str("hello world"), "HELLO WORLD"),
        ('GetDictValue', get_dict_value({"spam": "eggs"}, "spam"), "eggs"),
        ('GetDictValueWithDefault', get_dict_value_with_default({"spam": "eggs"}, "foo"), "default"),
        ('CombineLists', combine_lists([1, 2], [2, 3]), [1, 2, 2, 3]),
        ('CombineListsNoDuplicates', combine_lists_no_duplicates([1, 2], [2, 3]), [1, 2, 3]),
        ('IncrementInPlace', increment_in_place([1, 2, 3], 2), [3, 4, 5]),
        ('SumList', sum_list([1, 2, 3]), 6),
        ('LeftPad', left_pad('hello', 10), '00000hello'),
        ('FlattenDict', flatten_dict({"spam1": {"spam2": "spam3"}, "eggs1": {"eggs2": "eggs3"}}), {"spam1": "spam2.spam3", "eggs1": "eggs2.eggs3"}),
    ]

    for challenge in challenge_list:
        name = challenge[0]
        actual = challenge[1]
        expected = challenge[2]
        if actual == expected:
            print(f"{name}: PASSED")
        else:
            print(f"{name}: FAILED --- {actual} != {expected}")
            break
