
from __future__ import annotations

# Students may use the following standard-library tools where helpful:
from collections import Counter, defaultdict, OrderedDict, deque
import heapq
from math import gcd

def ex11_is_valid_sudoku(board: list[list[str]]) -> bool:
    """
    Check whether a Sudoku board is valid.

    Meaning:
    - A valid board does not repeat digits 1-9 in any row, column, or 3 x 3 box.
    - Empty cells are represented by '.'.
    - The board does not need to be fully solved.

    Suggested logic:
    1. Create three sets:
       - rows: stores (row_index, digit)
       - cols: stores (col_index, digit)
       - boxes: stores (box_row, box_col, digit)

    2. Loop over every cell board[r][c].
       - Skip if cell is '.'.
       - Compute box index:
           box_row = r // 3
           box_col = c // 3

    3. If the digit already exists in row, column, or box set, return False.

    4. Otherwise, add it to all three sets.

    5. If no duplicate is found, return True.

    Important points:
    - Only check validity of filled cells.
    - A board can be valid even if incomplete.
    """
    # TODO: Traverse all cells.
    # TODO: Ignore '.'.
    # TODO: Detect duplicates in row, column, and 3x3 box.
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for row in range(9):
        for col in range(9):
            value = board[row][col]
            if value == ".":
                continue

            box_index = (row//3, col//3)
            if value in rows[row] or value in cols[col] or value in boxes[box_index]:
                return False

            rows[row].add(value)
            cols[col].add(value)
            boxes[box_index].add(value)

    return True

def ex12_rearrange_no_adjacent(s: str) -> str | None:
    """
    Rearrange so no two adjacent characters are the same.
    Return None if impossible.

    Meaning:
    - Input: "aaabc"
      Possible output: "abaca"
    - No adjacent pair should contain the same character.

    Suggested logic using a max heap:
    1. Count frequency of each character.

    2. If the most frequent character appears more than (len(s) + 1) // 2 times,
       then rearrangement is impossible.
       Example: "aaaaab" cannot be rearranged validly.

    3. Use a max heap.
       - Python has min heap, so store negative frequencies.
       - Example: frequency 3 is stored as -3.

    4. Repeatedly pick the two most frequent different characters.
       - Add both to result.
       - Decrease their counts.
       - Push them back if they still remain.

    5. If one character remains at the end, append it.

    Important points:
    - Result may not be unique.
    - Tests should check validity, not exact string.
    - Empty string can return empty string.
    """
    # TODO: Count character frequency.
    # TODO: Check impossible condition.
    # TODO: Use a max heap or greedy placement strategy.
    # TODO: Return valid rearranged string or None.
    if not s:
        return ""
    # aaabc
    # a:3, b:1, c:1
    # a=best_char
    # 3=best_count
    # result = [a]
    # a:2, b:1, c:1
    # prev_char = a

    # b = best_char
    # 1 = best_count

    freq_counter = Counter(s)
    result = []
    prev = ""
    while len(result) < len(s):
        best_char = None
        best_count = 0
        for ch, count in freq_counter.items():
            if count > best_count and ch != prev:
                best_char = ch
                best_count = count

        if best_char is None:
            return None

        result.append(best_char)
        freq_counter[best_char] -= 1
        prev = best_char

    return "".join(result)


def ex13_k_closest_points(points: list[tuple[int, int]], k: int) -> list[tuple[int, int]]:
    """
    Return k closest points to origin (0, 0).

    Meaning:
    - Distance from origin for point (x, y) is sqrt(x^2 + y^2).
    - For comparison, we do not need sqrt.
      Squared distance = x^2 + y^2 is enough.

    Suggested logic:
    1. For each point, compute squared distance.
       Example: (1, 3) -> 1^2 + 3^2 = 10.

    2. Sort points by squared distance.

    3. Return first k points.

    Alternative efficient logic:
    - Use heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)

    Important points:
    - If k is 0, return empty list.
    - If k >= number of points, return all points sorted by distance.
    - Exact output order should be by increasing distance for these tests.
    """
    # TODO: Sort points using squared distance as key.
    # TODO: Return first k points.
    raise NotImplementedError


def ex14_word_pattern(pattern: str, s: str) -> bool:
    """
    Check if pattern matches words bijectively.

    Meaning:
    - Each character in pattern should map to exactly one word.
    - Each word should map back to exactly one pattern character.
    - This is called a bijection: one-to-one mapping in both directions.

    Example:
    pattern = "abba"
    s = "dog cat cat dog"
    Mapping:
    a -> dog
    b -> cat
    This is valid.

    Invalid example:
    pattern = "abba"
    s = "dog cat cat fish"
    a maps to both dog and fish, so invalid.

    Suggested logic:
    1. Split s into words.
    2. If length of pattern != number of words, return False.
    3. Use two dictionaries:
       - char_to_word
       - word_to_char
    4. For each pair (pattern_char, word):
       - Check consistency in both dictionaries.
       - If conflict appears, return False.
    5. Return True.
    """
    # TODO: Split s into words.
    # TODO: Check length mismatch.
    # TODO: Maintain both char_to_word and word_to_char mappings.
    s = s.split()
    if len(pattern) != len(s):
        return False

    char_to_word = {}
    word_to_char = {}

    # s = dog, cat, cat, dog
    # patt = abba
    #
    # ch = a
    # word = dog
    # char_to_word = {a:dog}
    # wprd_to_char = {dog: a}

    # ch = b
    # word = cat
    # char_to_word = {a:dog, b:cat}
    # wprd_to_char = {dog: a, cat:b}

    # ch = b
    # word = cat
    # char_to_word = {a:dog, b:cat}
    # wprd_to_char = {dog: a, cat:b}


    for ch, word in zip(pattern, s):
        if ch in char_to_word and char_to_word[ch] != word:
            return False

        if word in word_to_char and word_to_char[word] != ch:
            return False

        char_to_word[ch] = word
        word_to_char[word] = ch

    return True


def ex15_accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    """
    Merge accounts with common emails.

    Input format:
    - Each account is [name, email1, email2, ...]

    Meaning:
    - If two accounts share at least one email, they belong to the same person/account group.
    - All connected emails should be merged.

    Suggested logic using graph/DFS:
    1. Build an email graph.
       - Each email is a node.
       - Emails in the same account are connected.
       Example:
       ["John", "a@mail.com", "b@mail.com"] means a@mail.com connected to b@mail.com.

    2. Store email_to_name mapping.
       - This helps recover the account holder name for each email.

    3. Use DFS/BFS to find connected components.
       - Each connected component is one merged account.

    4. For each component:
       - Sort emails alphabetically.
       - Output [name] + sorted_emails.

    Important points:
    - Output order of accounts may vary; tests normalize it.
    - Email order inside each merged account should be sorted.
    - Accounts with only one email should still appear.
    """
    # TODO: Build graph connecting emails in the same account.
    # TODO: Traverse graph to find connected email groups.
    # TODO: Return [name] + sorted emails for each group.
    final_dict = {}
    for account in accounts:
        if account[0] not in final_dict:
            final_dict[account[0]] = set()
        for i in range(1, len(account)):
            for key in final_dict.keys():
                if key.lower() in account[i].lower():
                    final_dict[key].add(account[i])
                    break

    print(final_dict)

# =========================
# Test helpers
# =========================

def _normalize_grouped_lists(groups: list[list[str]]) -> list[list[str]]:
    """Sort inside each group and sort groups, so anagram group order does not matter."""
    return sorted([sorted(group) for group in groups])


def _normalize_accounts(accounts: list[list[str]]) -> list[list[str]]:
    """Sort emails inside each account and sort accounts for stable comparison."""
    cleaned = []
    for account in accounts:
        name = account[0]
        emails = sorted(account[1:])
        cleaned.append([name] + emails)
    return sorted(cleaned)


def _is_valid_no_adjacent_rearrangement(original: str, result: str | None) -> bool:
    """Check whether result uses same characters and has no equal adjacent characters."""
    if result is None:
        return False
    return sorted(original) == sorted(result) and all(
        result[i] != result[i + 1] for i in range(len(result) - 1)
    )


# =========================
# Tests
# =========================

def run_all_tests():
    """
    Run all tests.

    Student note:
    - At first, tests will fail because every function raises NotImplementedError.
    - Complete functions one by one.
    - After completing one function, you may temporarily comment out later tests.
    """

    # ex11: Valid Sudoku
    assert ex11_is_valid_sudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ] + [["."] * 9 for _ in range(6)]) is True
    assert ex11_is_valid_sudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "5"],
    ] + [["."] * 9 for _ in range(8)]) is False
    assert ex11_is_valid_sudoku([
        ["5", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", ".", "."],
    ] + [["."] * 9 for _ in range(7)]) is False

    # ex12: Rearrange no adjacent same characters
    result12 = ex12_rearrange_no_adjacent("aaabc")
    assert result12 == "abaca"
    assert ex12_rearrange_no_adjacent("aaaaab") is None
    result12b = ex12_rearrange_no_adjacent("aabb")
    assert result12b == "abab"
    assert ex12_rearrange_no_adjacent("") == ""

    # # ex13: K closest points
    # assert ex13_k_closest_points([(1, 3), (-2, 2), (5, 8), (0, 1)], 2) == [(0, 1), (-2, 2)]
    # assert ex13_k_closest_points([(3, 4), (0, 0), (1, 1)], 1) == [(0, 0)]
    # assert ex13_k_closest_points([(2, 2)], 5) == [(2, 2)]
    # assert ex13_k_closest_points([(1, 1)], 0) == []

    # ex14: Word pattern
    assert ex14_word_pattern("abba", "dog cat cat dog") is True
    assert ex14_word_pattern("abba", "dog cat cat fish") is False
    assert ex14_word_pattern("aaaa", "dog dog dog dog") is True
    assert ex14_word_pattern("abba", "dog dog dog dog") is False
    assert ex14_word_pattern("abc", "one two") is False

    # ex15: Accounts merge
    merged = ex15_accounts_merge([
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ])
    expected_merged = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com", "johnnybravo@mail.com"],
        ["Mary", "mary@mail.com"]
    ]
    assert _normalize_accounts(merged) == _normalize_accounts(expected_merged)

    merged2 = ex15_accounts_merge([
        ["A", "a1@mail.com", "a2@mail.com"],
        ["A", "a2@mail.com", "a3@mail.com"],
        ["B", "b1@mail.com"],
    ])
    expected_merged2 = [
        ["A", "a1@mail.com", "a2@mail.com", "a3@mail.com"],
        ["B", "b1@mail.com"],
    ]
    assert _normalize_accounts(merged2) == _normalize_accounts(expected_merged2)

    print("All Passed")


if __name__ == "__main__":
    run_all_tests()