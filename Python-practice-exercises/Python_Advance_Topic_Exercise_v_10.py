from __future__ import annotations
from collections import Counter
from typing import Any

def ex06_dict_keys_with_value(d: dict[str, int], target: int) -> list[str]:
    # final_list = []
    # for k,v in d.items():
    #     if v == target:
    #         final_list.append(k)

    return [k for k,v in d.items() if v==target]

def ex07_remove_duplicates_preserve_order(lst: list[Any]) -> list[Any]:
    final_list = []
    for item in lst:
        if item in final_list:
            continue
        final_list.append(item)
    return final_list


def ex08_tuple_max_second(pairs: list[tuple[int, int]]) -> tuple[int, int]:
    # max = 0
    # final_value = None
    # for a,b in pairs:
    #     if b > max:
    #         max = b
    #         final_value = (a,b)

    return max(pairs,key=lambda x:x[1])


def ex09_list_rotate_left(lst: list[int], k: int) -> list[int]:
    k = k % len(lst)
    return lst[k:] + lst[:k]


def ex10_set_symmetric_diff(a: set[int], b: set[int]) -> set[int]:
    final_list = set()
    for item in a:
        if item in b:
            b.remove(item)
            continue
        final_list.add(item)
    final_list = final_list.union(b)
    print(final_list)
    return final_list

# =========================
# Tests
# =========================

def run_all_tests():
    assert ex06_dict_keys_with_value({"a":1,"b":2,"c":1},1) == ["a","c"]
    assert ex07_remove_duplicates_preserve_order([1,2,1,3]) == [1,2,3]
    assert ex08_tuple_max_second([(1,2),(3,5),(0,1)]) == (3,5)
    assert ex09_list_rotate_left([1,2,3,4],1) == [2,3,4,1]
    assert ex10_set_symmetric_diff({1,2},{2,3}) == {1,3}
    print("✅ All tests passed!")
    run_all_tests()