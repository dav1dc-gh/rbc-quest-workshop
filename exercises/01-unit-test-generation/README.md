# Exercise 1: Unit Test Generation

## Objective

Learn how to prompt GitHub Copilot to generate **non-obvious** test cases — going beyond the "happy path" that any developer would immediately think of.

## The Problem

When you ask Copilot to "write tests for this function," it typically generates tests for:
- Normal valid inputs
- Maybe one empty input case
- Basic error conditions

But production bugs rarely come from these obvious scenarios. They come from **edge cases**, **boundary conditions**, and **unusual data combinations** that no one thought to test.

## Your Task

The file `src/date_range_calculator.py` contains a `DateRangeCalculator` class that computes business metrics over date ranges. A basic test file `tests/test_date_range_basic.py` has been started for you with only the most obvious tests.

Your job:
1. Review the source code in `src/date_range_calculator.py`
2. Look at the basic tests already provided
3. Use GitHub Copilot to generate a **comprehensive** test suite that covers non-obvious cases

## Getting Started

1. Open `src/date_range_calculator.py` and read through the implementation
2. Open `tests/test_date_range_basic.py` to see the obvious tests
3. Create a new file `tests/test_date_range_advanced.py`
4. Use Copilot Chat or inline comments to generate better tests

## The Secret

Simply asking "write tests" won't get you there. You need to **tell Copilot what kinds of edge cases to consider**. Think about:

- What happens at **timezone boundaries** (DST transitions)?
- What about **leap years** (Feb 29)?
- What about date ranges that **span year boundaries**?
- What about ranges where **start == end**?
- What about **weekends and holidays** in business day calculations?
- What about **very large ranges** (10+ years)?
- What about dates **far in the past** (before 1970)?

## Expected End State

You should have a `tests/test_date_range_advanced.py` file with **at least 15 test cases** covering non-obvious conditions. All tests should pass when run with:

```bash
cd exercises/01-unit-test-generation
pytest tests/ -v
```

## Hint

> The key insight is that you must **explicitly describe the edge case categories** you want Copilot to test. Try prompting with something like:
> "Generate test cases for boundary conditions including DST transitions, leap years, and single-day ranges"
> rather than just "write tests for this class."

**One thing you'll need to figure out on your own:** There's a subtle bug in the `get_business_days` method that only manifests with certain holiday configurations. Your advanced tests should catch it — but you'll need to think about what combination of inputs would expose it.
