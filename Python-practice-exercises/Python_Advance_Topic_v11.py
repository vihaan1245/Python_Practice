from __future__ import annotations
from collections import Counter
from typing import Any

def ex11_group_by_length(words: list[str]) -> dict[int, list[str]]:
    final_dict = {}
    for word in words:
        temp = final_dict.get(len(word), [])
        temp.append(word)
        final_dict[len(word)] = temp

    return final_dict


def ex12_find_duplicates(lst: list[int]) -> set[int]:
    # final_set = set()
    # duplicate_dict = Counter(lst)
    #
    # for k, v in duplicate_dict.items():
    #     if v >= 2:
    #         final_set.add(k)

    return {k for k,v in Counter(lst).items() if v>=2}


def ex13_flatten_tuple_list(data: list[tuple[int, int]]) -> list[int]:
    final_list = []
    for a,b in data:
        final_list.append(a)
        final_list.append(b)

    return final_list


def ex14_dict_max_key(d: dict[str, int]) -> str:
    max = 0
    max_k = ""
    for k,v in Counter(d).items():
        if v > max:
            max = v
            max_k = k

    return max_k


def ex15_split_even_odd(nums: list[int]) -> tuple[list[int], list[int]]:
    odd = []
    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return (even, odd)

# =========================
# Tests
# =========================

def run_all_tests():
    assert ex11_group_by_length(["a","bb","cc","d"]) == {1:["a","d"],2:["bb","cc"]}
    assert ex12_find_duplicates([1,2,2,3,3]) == {2,3}
    assert ex13_flatten_tuple_list([(1,2),(3,4)]) == [1,2,3,4]
    assert ex14_dict_max_key({"a":1,"b":5,"c":3}) == "b"
    assert ex15_split_even_odd([1,2,3,4]) == ([2,4],[1,3])
    print("✅ All tests passed!")

if __name__ == "__main__":
    run_all_tests()