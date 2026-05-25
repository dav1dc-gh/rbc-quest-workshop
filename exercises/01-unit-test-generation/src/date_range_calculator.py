"""
DateRangeCalculator - Computes business metrics over date ranges.

Handles business days, holiday exclusions, and date range overlaps.
"""

from datetime import date, timedelta
from typing import List, Optional, Tuple


class DateRangeCalculator:
    """Calculates various business metrics across date ranges."""

    def __init__(self, holidays: Optional[List[date]] = None):
        """
        Initialize with an optional list of holidays.

        Args:
            holidays: List of dates that are considered holidays (non-business days)
        """
        self.holidays = holidays or []

    def get_business_days(self, start: date, end: date) -> int:
        """
        Count the number of business days between start and end (inclusive).

        Business days exclude weekends (Saturday=5, Sunday=6) and any
        configured holidays.

        Args:
            start: Start date (inclusive)
            end: End date (inclusive)

        Returns:
            Number of business days in the range

        Raises:
            ValueError: If start is after end
        """
        if start > end:
            raise ValueError("Start date must be on or before end date")

        count = 0
        current = start
        while current <= end:
            if current.weekday() < 5 and current not in self.holidays:
                count += 1
            current += timedelta(days=1)
        return count

    def get_weekend_days(self, start: date, end: date) -> int:
        """
        Count weekend days in the range (inclusive).

        Args:
            start: Start date (inclusive)
            end: End date (inclusive)

        Returns:
            Number of Saturday/Sunday days in the range
        """
        if start > end:
            raise ValueError("Start date must be on or before end date")

        count = 0
        current = start
        while current <= end:
            if current.weekday() >= 5:
                count += 1
            current += timedelta(days=1)
        return count

    def get_date_range_overlap(
        self,
        range1: Tuple[date, date],
        range2: Tuple[date, date],
    ) -> Optional[Tuple[date, date]]:
        """
        Find the overlapping period between two date ranges.

        Args:
            range1: Tuple of (start, end) for first range
            range2: Tuple of (start, end) for second range

        Returns:
            Tuple of (start, end) of the overlap, or None if no overlap
        """
        start1, end1 = range1
        start2, end2 = range2

        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)

        if overlap_start <= overlap_end:
            return (overlap_start, overlap_end)
        return None

    def split_range_by_month(self, start: date, end: date) -> List[Tuple[date, date]]:
        """
        Split a date range into sub-ranges by calendar month.

        Args:
            start: Start date
            end: End date

        Returns:
            List of (start, end) tuples, one per month segment
        """
        if start > end:
            raise ValueError("Start date must be on or before end date")

        segments = []
        current_start = start

        while current_start <= end:
            # Find end of current month
            if current_start.month == 12:
                month_end = date(current_start.year + 1, 1, 1) - timedelta(days=1)
            else:
                month_end = date(current_start.year, current_start.month + 1, 1) - timedelta(days=1)

            segment_end = min(month_end, end)
            segments.append((current_start, segment_end))

            # Move to first day of next month
            current_start = segment_end + timedelta(days=1)

        return segments

    def calculate_utilization(self, start: date, end: date, days_worked: int) -> float:
        """
        Calculate utilization rate as a percentage.

        Utilization = days_worked / business_days * 100

        Args:
            start: Period start date
            end: Period end date
            days_worked: Number of days actually worked

        Returns:
            Utilization percentage (0.0 to 100.0+)

        Raises:
            ValueError: If days_worked is negative
            ZeroDivisionError: If there are no business days in the range
        """
        if days_worked < 0:
            raise ValueError("Days worked cannot be negative")

        business_days = self.get_business_days(start, end)
        return (days_worked / business_days) * 100

    def get_next_business_day(self, from_date: date) -> date:
        """
        Get the next business day on or after the given date.

        Args:
            from_date: The starting date

        Returns:
            The next date that is a business day
        """
        current = from_date
        while current.weekday() >= 5 or current in self.holidays:
            current += timedelta(days=1)
        return current

    def count_holidays_in_range(self, start: date, end: date) -> int:
        """
        Count configured holidays that fall within the date range.

        Note: Only counts holidays that fall on weekdays (holidays on
        weekends are not counted as they're already non-business days).

        Args:
            start: Start date (inclusive)
            end: End date (inclusive)

        Returns:
            Number of weekday holidays in the range
        """
        if start > end:
            raise ValueError("Start date must be on or before end date")

        count = 0
        for holiday in self.holidays:
            if start <= holiday <= end and holiday.weekday() < 5:
                count += 1
        return count
