from __future__ import annotations
from collections import Counter, defaultdict
from typing import Any


def ex01_group_anagrams(words: list[str]) -> list[list[str]]:
    """Group anagrams together."""
    # TODO
    final_dict = {}
    for word in words:
        sorted_word = sorted(word)
        sorted_word = "".join(sorted_word)
        if sorted_word in final_dict:
            final_dict[sorted_word].append(word)
        else:
            final_dict[sorted_word] = [word]

    return (list(final_dict.values()))


def ex02_top_k_frequent(nums: list[int], k: int) -> list[int]:
    # final_dict = Counter(nums)
    # final_list = []
    # sliced_dict = (sorted(final_dict.items(), key=lambda x: x[1], reverse=True)[:k])
    #
    # for a,b in sliced_dict:
    #     final_list.append(a)

    return [num for num, count in Counter(nums).most_common(k)]

def ex03_merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    final_list = []
    intervals.sort()
    first = intervals[0]
    for a,b in intervals[1:]:
        if a <= first[1]:
            final_list.append((first[0],b))
        else:
            final_list.append((a,b))
        first = (a,b)

    return final_list



def ex04_longest_consecutive(nums: list[int]) -> int:
    """Return length of longest consecutive sequence."""
    # TODO
    nums = sorted(nums)
    final_list = []
    consecutive_len = 1
    current_num = nums[0]
    for num in nums[1:]:
        if current_num+1 == num:
            consecutive_len += 1
        else:
            final_list.append(consecutive_len)
            consecutive_len = 1
        current_num = num

    return max(final_list)


def ex05_subarray_sum_k(nums: list[int], k: int) -> int:
    """Count subarrays whose sum equals k."""
    # TODO
    count = 0
    for i in range(1,len(nums)):
        if nums[i]+nums[i-1] == k:
            count += 1

    return count

# =========================
# Tests
# =========================

def run_all_tests():
    assert ex01_group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
    assert set(ex02_top_k_frequent([1,1,1,2,2,3],2)) == {1,2}
    assert set(ex02_top_k_frequent([12,12,12,15,15,16,16,16,16], 2)) == {12,16}
    assert ex03_merge_intervals([(1,3),(2,6),(8,10)]) == [(1,6),(8,10)]
    assert ex04_longest_consecutive([100,4,200,1,3,2]) == 4
    assert ex05_subarray_sum_k([1,1,1],2) == 2
    print("✅ All tests passed!")
    


if __name__ == "__main__":
    run_all_tests()