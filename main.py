#!/usr/bin/env python3
"""
This code is not meant to be altered. Please open assessment.py
"""
import sys
sys.path.append('.')
from assessment import *

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

    index = 0
    for challenge in challenge_list:
        index += 1
        name = challenge[0]
        actual = challenge[1]
        expected = challenge[2]
        if actual == expected:
            print(f"{index}. {name}: PASSED")
        else:
            print(f"{index}. {name}: FAILED --- {actual} != {expected}")

