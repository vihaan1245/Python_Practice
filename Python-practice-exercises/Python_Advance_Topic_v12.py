
from __future__ import annotations
from collections import Counter
from typing import Any



def ex16_char_frequency(s: str) -> dict[str, int]:
    # final_list = []
    # for char in s:
    #     final_list.append(char)

    return Counter([char for char in s])


def ex17_filter_long_words(words: list[str], k: int) -> list[str]:
    return [word for word in words if len(word) > k]


def ex18_tuple_to_dict(pairs: list[tuple[str, int]]) -> dict[str, int]:
    return {a:b for a,b in pairs}


def ex19_intersection_multiple(sets: list[set[int]]) -> set[int]:
    final_set = set()
    final_list = []
    for set_val in sets:
        for val in set_val:
            final_list.append(val)


    for k,v in Counter(final_list).items():
        if v > 2:
            final_set.add(k)

    return final_set


def ex20_running_max(nums: list[int]) -> list[int]:
    # final_list = []
    # temp = 0
    # for num in nums:
    #     if num >= temp:
    #         final_list.append(num)
    #     else:
    #         final_list.append(temp)
    #     temp = num

    temp = nums[0]
    for i in range(1, len(nums)):
        if temp > nums[i]:
            nums[i] = temp
        temp = nums[i]
    return nums


# =========================
# Tests
# =========================

def run_all_tests():    
    assert ex16_char_frequency("aab") == {"a":2,"b":1}
    assert ex17_filter_long_words(["hi","hello","world"],3) == ["hello","world"]
    assert ex18_tuple_to_dict([("a",1),("b",2)]) == {"a":1,"b":2}
    assert ex19_intersection_multiple([{1,2,3},{2,3},{3,4}]) == {3}
    assert ex20_running_max([1,3,2,5]) == [1,3,3,5]

    print("✅ All tests passed!")


if __name__ == "__main__":
    run_all_tests()