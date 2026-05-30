from __future__ import annotations


def ex06_group_by_anagram_count(words: list[str]) -> dict[int, list[str]]:
    """
    Group words by the number of unique characters.

    Example:
        words = ["abc", "aab", "xyz"]

        "abc" has unique characters {'a', 'b', 'c'} -> count = 3
        "aab" has unique characters {'a', 'b'}      -> count = 2
        "xyz" has unique characters {'x', 'y', 'z'} -> count = 3

        Output:
        {
            3: ["abc", "xyz"],
            2: ["aab"]
        }

    Main idea:
    - A set stores only unique values.
    - If we convert a word into a set, repeated characters are automatically removed.
    - The length of that set gives the number of unique characters in the word.
    - We use that count as the key in a dictionary.
    - The dictionary value should be a list of all words having that many unique characters.

    Step-by-step logic:
    1. Create an empty dictionary, for example: grouped = {}
    2. Loop through every word in the input list.
    3. Convert the word to a set:
           unique_chars = set(word)
    4. Count the number of unique characters:
           count = len(unique_chars)
    5. If count is not already present as a key in the dictionary:
           create a new empty list for that count.
    6. Append the current word to the list for that count.
    7. Return the final dictionary.

    Important note:
    - The order of words inside each group should follow the original input order.
    - Empty string "" has 0 unique characters.
    """
    # TODO:
    # 1. Create an empty dictionary named grouped.
    # 2. For each word in words:
    #       a. Find the number of unique characters using len(set(word)).
    #       b. If this count is not already a key in grouped, create grouped[count] = [].
    #       c. Append the word to grouped[count].
    # 3. Return grouped.
    #
    # Hint:
    # You may use either:
    #       if count not in grouped:
    #           grouped[count] = []
    #
    # Or:
    #       grouped.setdefault(count, []).append(word)
    grouped = {}
    for word in words:
        count = len(set(word))
        if count not in grouped:
            grouped[count] = []
        grouped[count].append(word)
    return grouped


def ex07_lru_simulation(ops: list[tuple[str, int]], capacity: int) -> list[int]:
    """
    Simulate an LRU cache.

    LRU meaning:
    - LRU stands for Least Recently Used.
    - When the cache is full and we need to insert a new item,
      we remove the item that has not been used for the longest time.

    Input format:
        ops is a list of operations.
        Each operation is a tuple:
            ("put", key) -> insert key into cache
            ("get", key) -> access key from cache

    For simplicity:
    - The key and value are considered the same.
    - So if key = 5 is present, get operation returns 5.
    - If key is not present, get operation returns -1.

    Example:
        ops = [
            ("put", 1),
            ("put", 2),
            ("get", 1),
            ("put", 3),
            ("get", 2),
            ("get", 3)
        ]
        capacity = 2

    Dry run:
        put 1 -> cache: [1]
        put 2 -> cache: [1, 2]
        get 1 -> returns 1, key 1 becomes most recently used
                 cache order becomes [2, 1]
        put 3 -> cache is full, remove least recently used key 2
                 cache becomes [1, 3]
        get 2 -> key 2 not found, return -1
        get 3 -> returns 3

        Output: [1, -1, 3]

    Main idea:
    - We need to maintain usage order.
    - The front/first item should represent the least recently used key.
    - The end/last item should represent the most recently used key.
    - Python's collections.OrderedDict is useful because:
          1. It remembers insertion order.
          2. It allows moving a key to the end using move_to_end(key).
          3. It allows removing the first item using popitem(last=False).

    Step-by-step logic:
    1. Import OrderedDict from collections.
    2. Create an empty OrderedDict called cache.
    3. Create an empty list called result to store outputs of get operations.
    4. Process each operation one by one.
    5. If operation is "get":
           a. If key exists in cache:
                - Move it to the end because it is now recently used.
                - Append key to result.
           b. If key does not exist:
                - Append -1 to result.
    6. If operation is "put":
           a. If capacity is 0, cache cannot store anything. Ignore the put.
           b. If key already exists:
                - Move it to the end because updating/accessing makes it recently used.
           c. Insert/update cache[key] = key.
           d. If cache size becomes greater than capacity:
                - Remove least recently used item from the front.
    7. Return result.

    Important edge cases:
    - capacity = 0 means no item can be stored.
    - putting an already existing key should refresh its recent-use position.
    - Only "get" operations produce output.
    """
    # TODO:
    # 1. Import OrderedDict inside or outside the function.
    # 2. Initialize:
    #       cache = OrderedDict()
    #       result = []
    # 3. Loop through each (operation, key) in ops.
    # 4. For "get":
    #       if key is present:
    #           move key to end
    #           append key to result
    #       else:
    #           append -1 to result
    # 5. For "put":
    #       if capacity == 0:
    #           continue
    #       if key already exists:
    #           move key to end
    #       set cache[key] = key
    #       if len(cache) > capacity:
    #           remove the first item using popitem(last=False)
    # 6. Return result.
    cache = []
    result = []

    for operation,key in ops:
        if operation == "get":
            if key in cache:
                cache.remove(key)
                cache.append(key)
                result.append(key)
            else:
                result.append(-1)

        elif operation == "put":
            if capacity == 0:
                continue
            if key in cache:
                cache.remove(key)
            cache.append(key)

            if len(cache) > capacity:
                cache.pop(0)

    return result



def ex08_matrix_spiral(matrix: list[list[int]]) -> list[int]:
    """
    Return spiral order traversal of a matrix.

    Spiral order means:
    - Start from the top-left corner.
    - Move from left to right along the top row.
    - Then move top to bottom along the rightmost column.
    - Then move right to left along the bottom row.
    - Then move bottom to top along the leftmost column.
    - Continue this process inward until all elements are visited.

    Example:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        Spiral order:
        1, 2, 3, 6, 9, 8, 7, 4, 5

    Main idea:
    Use four boundary variables:
        top    -> index of the current top row
        bottom -> index of the current bottom row
        left   -> index of the current left column
        right  -> index of the current right column

    Step-by-step logic:
    1. If matrix is empty, return an empty list.
    2. Initialize boundaries:
           top = 0
           bottom = number of rows - 1
           left = 0
           right = number of columns - 1
    3. Create an empty list called result.
    4. Continue while top <= bottom and left <= right.
    5. Traverse the top row from left to right.
           After this, increase top by 1 because that row is completed.
    6. Traverse the right column from top to bottom.
           After this, decrease right by 1 because that column is completed.
    7. Before traversing the bottom row, check whether top <= bottom.
           This avoids duplicate traversal in a single remaining row.
    8. Traverse the bottom row from right to left.
           After this, decrease bottom by 1.
    9. Before traversing the left column, check whether left <= right.
           This avoids duplicate traversal in a single remaining column.
    10. Traverse the left column from bottom to top.
           After this, increase left by 1.
    11. Return result.

    Important edge cases:
    - Empty matrix: []
    - Single row matrix: [[1, 2, 3]]
    - Single column matrix: [[1], [2], [3]]
    - Rectangular matrix, not only square matrix.
    """
    # TODO:
    # 1. Handle empty matrix.
    # 2. Initialize top, bottom, left, and right boundaries.
    # 3. Use a while loop to continue while boundaries are valid.
    # 4. Traverse:
    #       a. top row
    #       b. right column
    #       c. bottom row, only if top <= bottom
    #       d. left column, only if left <= right
    # 5. Shrink boundaries after each side traversal.
    # 6. Return result.

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         print(matrix[i][j])
    if not matrix:
        return []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    result = []

    while (top <= bottom) and (left <= right):
        for col in range(left, right+1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom+1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left -1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
            left += 1
    return result

def ex09_pair_sum_all(nums: list[int], target: int) -> list[tuple[int, int]]:
    """
    Return all unique pairs whose sum is equal to target.

    Example:
        nums = [1, 2, 3, 4, 5]
        target = 5

        Valid pairs:
            1 + 4 = 5
            2 + 3 = 5

        Output:
            [(1, 4), (2, 3)]

    Main idea:
    - For each number x, we need another number y such that:
          x + y = target
      Therefore:
          y = target - x

    - We can use a set called seen to remember numbers already visited.
    - For each current number:
          complement = target - current_number
      If complement is already in seen, we found a valid pair.

    Why store pair in sorted form?
    - Suppose we find pair (4, 1), it is the same as (1, 4).
    - To avoid duplicates, always store pairs as:
          (min(number, complement), max(number, complement))

    Why use another set for pairs?
    - The input may contain repeated numbers.
    - A result set prevents duplicate pairs from being stored multiple times.

    Step-by-step logic:
    1. Create an empty set called seen.
    2. Create an empty set called pairs.
    3. Loop through each number in nums.
    4. Calculate complement = target - number.
    5. If complement exists in seen:
           a. Create ordered_pair = (min(number, complement), max(number, complement)).
           b. Add ordered_pair to pairs.
    6. Add current number to seen.
    7. Convert pairs to a list and return it.

    Important edge cases:
    - Duplicate numbers, for example [2, 2, 2] with target 4.
    - Negative numbers, for example [-1, 4, 6] with target 5.
    - No valid pair should return an empty list.
    """
    # TODO:
    # 1. Create seen = set().
    # 2. Create pairs = set().
    # 3. For each number in nums:
    #       a. complement = target - number
    #       b. if complement in seen:
    #              ordered_pair = (min(number, complement), max(number, complement))
    #              add ordered_pair to pairs
    #       c. add number to seen
    # 4. Return list(pairs).
    #
    # Note:
    # The order of pairs in the returned list is not important for the tests,
    # because the tests convert your answer to a set.
    seen = set()
    pairs = set()
    for number in nums:
        complement = target-number
        if complement in seen:
            ordered_pair = (complement,number)
            pairs.add(ordered_pair)
        seen.add(number)
    print(pairs)
    return list(pairs)



def ex10_min_window_substring(s: str, t: str) -> str:
    """
    Return the minimum window substring of s that contains all characters of t.

    Problem meaning:
    - We are given two strings:
          s -> main string
          t -> required characters
    - We need the smallest substring of s that contains every character of t.
    - Character frequency matters.

    Example:
        s = "ADOBECODEBANC"
        t = "ABC"

        The minimum substring containing A, B, and C is:
        "BANC"

    Frequency example:
        s = "AAABBC"
        t = "AABC"

        t requires:
            A -> 2 times
            B -> 1 time
            C -> 1 time

        So the window must contain at least two A's, one B, and one C.

    Main idea:
    - This is a sliding window problem.
    - We use two pointers:
          left  -> start of current window
          right -> end of current window
    - We expand the right pointer to include more characters.
    - Once the window contains all required characters, we shrink from the left
      to make the window as small as possible.

    Helpful data structures:
    - Counter(t) stores required character frequencies.
    - Another dictionary or Counter stores current window frequencies.

    Important variables:
    - required:
          Number of distinct characters needed.
          Example: t = "AABC" has distinct characters A, B, C, so required = 3.

    - formed:
          Number of distinct characters that currently satisfy the required frequency.
          Example:
              If current window has A twice and t needs A twice,
              then A is satisfied.

    Step-by-step logic:
    1. If s or t is empty, return "".
    2. Count required characters using Counter(t).
    3. Initialize:
           window_counts = {}
           required = len(required_counts)
           formed = 0
           left = 0
           best_length = infinity
           best_start = 0
    4. Move right pointer from 0 to len(s)-1.
    5. Add s[right] to window_counts.
    6. If s[right] is a required character and its count now matches the required count:
           increase formed by 1.
    7. While formed == required:
           a. Current window is valid.
           b. Update best answer if current window is smaller.
           c. Try to remove s[left] from the window.
           d. If removing s[left] makes a required character count too small:
                  decrease formed by 1.
           e. Move left pointer forward.
    8. After the loop, if no valid window was found, return "".
       Otherwise return s[best_start : best_start + best_length].

    Important edge cases:
    - t is longer than s.
    - t contains repeated characters.
    - no valid window exists.
    - exact match, where s itself is the answer.
    """
    # TODO:
    # 1. Handle empty string cases.
    # 2. Use Counter from collections to count characters in t.
    # 3. Use a dictionary/Counter to count characters in current window.
    # 4. Use right pointer to expand the window.
    # 5. Use formed to know when all required frequencies are satisfied.
    # 6. When formed == required:
    #       a. update the best/smallest window
    #       b. shrink from the left side
    # 7. Return the smallest valid substring, or "" if no such substring exists.
    raise NotImplementedError


# =========================
# Tests
# =========================

def run_all_tests():
    """
    Run all test cases.

    Note for students:
    - These tests are written using assert statements.
    - If an assert fails, Python will stop and show an AssertionError.
    - That means your function output does not match the expected output.
    - If all tests pass, the final print statement will run.
    """

    # -------------------------
    # ex06_group_by_anagram_count tests
    # -------------------------

    # Basic case: words are grouped by number of unique characters.
    assert ex06_group_by_anagram_count(["abc", "aab", "xyz"]) == {
        3: ["abc", "xyz"],
        2: ["aab"]
    }

    # Repeated characters: "aaaa" has only 1 unique character.
    assert ex06_group_by_anagram_count(["aaaa", "bb", "abc", "abca"]) == {
        1: ["aaaa", "bb"],
        3: ["abc", "abca"]
    }

    # Empty input list should return an empty dictionary.
    assert ex06_group_by_anagram_count([]) == {}

    # Empty string has 0 unique characters.
    assert ex06_group_by_anagram_count(["", "a", "ab", "aa"]) == {
        0: [""],
        1: ["a", "aa"],
        2: ["ab"]
    }

    # Case sensitivity: uppercase and lowercase letters are different in Python.
    assert ex06_group_by_anagram_count(["Aa", "aa", "ABC", "AAB"]) == {
        1: ["aa"],
        2: ["Aa", "AAB"],
        3: ["ABC"]
    }

    # -------------------------
    # # ex07_lru_simulation tests
    # # -------------------------
    #
    # Basic LRU behavior.
    assert ex07_lru_simulation(
        [("put", 1), ("put", 2), ("get", 1), ("put", 3), ("get", 2), ("get", 3)],
        2
    ) == [1, -1, 3]

    # Getting a missing key should return -1.
    assert ex07_lru_simulation(
        [("get", 10), ("put", 10), ("get", 10)],
        1
    ) == [-1, 10]

    # Capacity 0 means nothing can be stored.
    assert ex07_lru_simulation(
        [("put", 1), ("get", 1), ("put", 2), ("get", 2)],
        0
    ) == [-1, -1]

    # Updating/putting an existing key should make it recently used.
    assert ex07_lru_simulation(
        [("put", 1), ("put", 2), ("put", 1), ("put", 3), ("get", 1), ("get", 2), ("get", 3)],
        2
    ) == [1, -1, 3]

    # More evictions with capacity 2.
    assert ex07_lru_simulation(
        [("put", 1), ("put", 2), ("put", 3), ("get", 1), ("get", 2), ("get", 3)],
        2
    ) == [-1, 2, 3]

    # -------------------------
    # ex08_matrix_spiral tests
    # -------------------------

    # Square matrix.
    assert ex08_matrix_spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1, 2, 3, 6, 9, 8, 7, 4, 5
    ]

    # Empty matrix.
    assert ex08_matrix_spiral([]) == []

    # Single row matrix.
    assert ex08_matrix_spiral([[1, 2, 3, 4]]) == [1, 2, 3, 4]

    # Single column matrix.
    assert ex08_matrix_spiral([[1], [2], [3], [4]]) == [1, 2, 3, 4]

    # Rectangular matrix with more columns than rows.
    assert ex08_matrix_spiral([[1, 2, 3, 4], [5, 6, 7, 8]]) == [
        1, 2, 3, 4, 8, 7, 6, 5
    ]

    # Rectangular matrix with more rows than columns.
    assert ex08_matrix_spiral([[1, 2], [3, 4], [5, 6]]) == [
        1, 2, 4, 6, 5, 3
    ]

    # -------------------------
    # ex09_pair_sum_all tests
    # -------------------------

    # Basic pair-sum case.
    assert set(ex09_pair_sum_all([1, 2, 3, 4, 5], 5)) == {(1, 4), (2, 3)}

    # Duplicate values should not create duplicate pairs.
    assert set(ex09_pair_sum_all([2, 2, 2, 2], 4)) == {(2, 2)}

    # Negative numbers.
    assert set(ex09_pair_sum_all([-1, 0, 1, 2, 3, 4], 3)) == {(-1, 4), (0, 3), (1, 2)}

    # No pair exists.
    assert set(ex09_pair_sum_all([10, 20, 30], 15)) == set()

    # Same number can form a pair only if it appears at least twice.
    assert set(ex09_pair_sum_all([1, 3, 3, 5], 6)) == {(1, 5), (3, 3)}
    #
    # # -------------------------
    # # ex10_min_window_substring tests
    # # -------------------------
    #
    # # Standard case.
    # assert ex10_min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    #
    # # Exact match.
    # assert ex10_min_window_substring("ABC", "ABC") == "ABC"
    #
    # # No valid window exists.
    # assert ex10_min_window_substring("A", "AA") == ""
    #
    # # Empty t should return empty string.
    # assert ex10_min_window_substring("ABC", "") == ""
    #
    # # Empty s should return empty string.
    # assert ex10_min_window_substring("", "ABC") == ""
    #
    # # Repeated character requirement.
    # assert ex10_min_window_substring("AAABBC", "AABC") == "AABBC"
    #
    # # Smallest window appears near the end.
    # assert ex10_min_window_substring("this is a test string", "tist") == "t stri"

    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_all_tests()
