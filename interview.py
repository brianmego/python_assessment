def get_list_index(inp: list, index: int):
    """
    input:
        inp: [1, 2, 3]
        index: 2
    expected: 3
    """
    pass


def uppercase_str(inp: str):
    """
    input:
        inp: 'hello world'
    expected: HELLO WORLD
    """
    pass


def get_dict_value(inp: dict, key: str):
    """
    input:
        inp: {
            "spam": "eggs"
        }
        key: "spam"
    expected: "eggs"
    """
    pass


def get_dict_value_with_default(inp: dict, key: str):
    """
    input:
        inp: {
            "spam": "eggs"
        }
        key: "spam"
    expected: "default"
    """
    pass


def combine_lists(inp: list, inp2: list):
    """
    input:
        inp: [1, 2],
        inp2: [2, 3]
    expected: [1, 2, 2, 3]
    """
    pass


def combine_lists_no_duplicates(inp: list, inp2: list):
    """
    input:
        inp: [1, 2],
        inp2: [2, 3]
    expected: [1, 2, 3]
    """
    pass


def increment_in_place(inp: list, inc_value: int):
    """
    input:
        inp: [1, 2, 3]
        inc_value: 2
    expected: [3, 4, 5]
    """
    ### Untouchable ###
    _orig_id = id(inp)
    _orig = inp
    ### /Untouchable ###

    # Your Code
    # Your Code
    # Your Code

    ### Untouchable ###
    if id(inp) != _orig_id:
        return _orig
    return inp
    ### /Untouchable ###


def sum_list(inp: list):
    """
    input:
        inp: [1, 2, 3]
    expected==6
    """
    pass


def left_pad(inp: str, pad_length: int):
    """
    input:
        inp: 'hello'
        pad_length: 10
    expected==00000hello
    """
    pass


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
    pass


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
