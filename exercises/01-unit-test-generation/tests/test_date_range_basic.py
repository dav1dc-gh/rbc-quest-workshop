"""Basic tests for DateRangeCalculator - these are the obvious ones."""

import pytest
from datetime import date
from src.date_range_calculator import DateRangeCalculator


class TestBasicBusinessDays:
    """Obvious test cases that anyone would write."""

    def test_full_work_week(self):
        calc = DateRangeCalculator()
        # Monday to Friday
        result = calc.get_business_days(date(2024, 1, 8), date(2024, 1, 12))
        assert result == 5

    def test_includes_weekend(self):
        calc = DateRangeCalculator()
        # Monday to next Monday (includes Sat + Sun)
        result = calc.get_business_days(date(2024, 1, 8), date(2024, 1, 15))
        assert result == 6

    def test_invalid_range_raises(self):
        calc = DateRangeCalculator()
        with pytest.raises(ValueError):
            calc.get_business_days(date(2024, 1, 15), date(2024, 1, 8))

    def test_single_weekday(self):
        calc = DateRangeCalculator()
        result = calc.get_business_days(date(2024, 1, 8), date(2024, 1, 8))
        assert result == 1

    def test_single_weekend_day(self):
        calc = DateRangeCalculator()
        result = calc.get_business_days(date(2024, 1, 6), date(2024, 1, 6))
        assert result == 0


class TestBasicOverlap:
    """Obvious overlap tests."""

    def test_full_overlap(self):
        calc = DateRangeCalculator()
        result = calc.get_date_range_overlap(
            (date(2024, 1, 1), date(2024, 1, 31)),
            (date(2024, 1, 10), date(2024, 1, 20)),
        )
        assert result == (date(2024, 1, 10), date(2024, 1, 20))

    def test_no_overlap(self):
        calc = DateRangeCalculator()
        result = calc.get_date_range_overlap(
            (date(2024, 1, 1), date(2024, 1, 10)),
            (date(2024, 2, 1), date(2024, 2, 10)),
        )
        assert result is None

    def test_adjacent_ranges(self):
        calc = DateRangeCalculator()
        result = calc.get_date_range_overlap(
            (date(2024, 1, 1), date(2024, 1, 10)),
            (date(2024, 1, 10), date(2024, 1, 20)),
        )
        assert result == (date(2024, 1, 10), date(2024, 1, 10))
