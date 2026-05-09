
from __future__ import annotations
from collections import Counter
from typing import Any


def ex01_unique_sorted(nums: list[int]) -> list[int]:
    final_list = []
    for num in nums:
        if num in final_list:
            continue
        final_list.append(num)

    return sorted(final_list)

def ex02_dict_sum_values(d: dict[str, int]) -> int:
    sum_of_d = 0
    for k,v in d.items():
        sum_of_d += v

    return sum_of_d


def ex03_common_elements(a: list[int], b: list[int]) -> list[int]:
    final_list = []
    for element in a:
        for num in b:
            if element == num:
                final_list.append(element)

    return final_list


def ex04_tuple_swap_pairs(pairs: list[tuple[int, int]]) -> list[tuple[int, int]]:
    final_list = []
    for a,b in pairs:
        final_list.append((b,a))

    return final_list


def ex05_count_even(nums: list[int]) -> int:
    final_list = [num for num in nums if num % 2 ==0]
    return len(final_list)


# =========================
# Tests
# =========================

def run_all_tests():
    assert ex01_unique_sorted([3,1,2,3]) == [1,2,3]
    assert ex02_dict_sum_values({"a":1,"b":2}) == 3
    assert ex03_common_elements([1,2,3],[2,3,4]) == [2,3]
    assert ex04_tuple_swap_pairs([(1,2),(3,4)]) == [(2,1),(4,3)]
    assert ex05_count_even([1,2,4,5]) == 2
    

    print("✅ All tests passed!")
if __name__ == "__main__":
    run_all_tests()