"""
Tests that verify your clean_code.py produces identical results to mystery_code.py.
All tests must pass after you complete your refactoring.
"""

import pytest
from src.mystery_code import fn1, fn2, fn3


class TestFn1Equivalence:
    """Tests for the first function."""

    def get_clean_fn1(self):
        from src.clean_code import sort_array  # noqa: expected function name
        return sort_array

    def test_basic_unsorted(self):
        clean = self.get_clean_fn1()
        data = [3, 6, 8, 10, 1, 2, 1]
        assert clean(data[:]) == fn1(data[:])

    def test_already_sorted(self):
        clean = self.get_clean_fn1()
        data = [1, 2, 3, 4, 5]
        assert clean(data[:]) == fn1(data[:])

    def test_reverse_sorted(self):
        clean = self.get_clean_fn1()
        data = [5, 4, 3, 2, 1]
        assert clean(data[:]) == fn1(data[:])

    def test_duplicates(self):
        clean = self.get_clean_fn1()
        data = [4, 2, 4, 1, 2, 4, 1]
        assert clean(data[:]) == fn1(data[:])

    def test_single_element(self):
        clean = self.get_clean_fn1()
        data = [42]
        assert clean(data[:]) == fn1(data[:])

    def test_empty_list(self):
        clean = self.get_clean_fn1()
        data = []
        assert clean(data[:]) == fn1(data[:])

    def test_negative_numbers(self):
        clean = self.get_clean_fn1()
        data = [-3, -1, -7, 0, 2, -5]
        assert clean(data[:]) == fn1(data[:])


class TestFn2Equivalence:
    """Tests for the second function."""

    def get_clean_fn2(self):
        from src.clean_code import find_combinations  # noqa: expected function name
        return find_combinations

    def test_basic_combination(self):
        clean = self.get_clean_fn2()
        data = [2, 3, 6, 7]
        assert clean(data[:], 7) == fn2(data[:], 7)

    def test_with_duplicates(self):
        clean = self.get_clean_fn2()
        data = [10, 1, 2, 7, 6, 1, 5]
        assert clean(data[:], 8) == fn2(data[:], 8)

    def test_no_solution(self):
        clean = self.get_clean_fn2()
        data = [5, 10, 15]
        assert clean(data[:], 3) == fn2(data[:], 3)

    def test_single_element_solution(self):
        clean = self.get_clean_fn2()
        data = [1, 2, 3]
        assert clean(data[:], 3) == fn2(data[:], 3)

    def test_empty_input(self):
        clean = self.get_clean_fn2()
        data = []
        assert clean(data[:], 5) == fn2(data[:], 5)

    def test_target_zero(self):
        clean = self.get_clean_fn2()
        data = [1, 2, 3]
        assert clean(data[:], 0) == fn2(data[:], 0)


class TestFn3Equivalence:
    """Tests for the third function."""

    def get_clean_fn3(self):
        from src.clean_code import longest_palindrome  # noqa: expected function name
        return longest_palindrome

    def test_basic_palindrome(self):
        clean = self.get_clean_fn3()
        assert clean("babad") == fn3("babad")

    def test_full_palindrome(self):
        clean = self.get_clean_fn3()
        assert clean("racecar") == fn3("racecar")

    def test_single_char(self):
        clean = self.get_clean_fn3()
        assert clean("a") == fn3("a")

    def test_two_chars_same(self):
        clean = self.get_clean_fn3()
        assert clean("bb") == fn3("bb")

    def test_two_chars_diff(self):
        clean = self.get_clean_fn3()
        assert clean("ab") == fn3("ab")

    def test_long_string(self):
        clean = self.get_clean_fn3()
        s = "forgeeksskeegfor"
        assert clean(s) == fn3(s)

    def test_no_palindrome_longer_than_one(self):
        clean = self.get_clean_fn3()
        assert clean("abcde") == fn3("abcde")

    def test_even_length_palindrome(self):
        clean = self.get_clean_fn3()
        assert clean("abccba") == fn3("abccba")
