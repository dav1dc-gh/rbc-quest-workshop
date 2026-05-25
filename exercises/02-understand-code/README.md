# Exercise 2: Understand Code

## Objective

Use GitHub Copilot to **explain** and then **refactor** highly complex, unreadable code into clean, maintainable implementations — while preserving identical behavior.

## The Problem

Real-world codebases often contain code written by developers who prioritized brevity over clarity, or code that has evolved over years without refactoring. This code works, but:

- Variable names are single characters with no meaning
- Multiple operations are crammed onto single lines
- There are no comments explaining intent
- Complex logic is nested deeply without helper functions

GitHub Copilot can help you **understand** what this code does and **refactor** it — but you need to verify the behavior is preserved.

## Your Task

The file `src/mystery_code.py` contains three functions that are deliberately obfuscated. They all work correctly but are nearly impossible to read.

Your job:
1. Use Copilot to **explain** what each function does
2. Write a brief comment above each function documenting its purpose
3. **Refactor** each function into clean, readable code in a new file `src/clean_code.py`
4. Ensure your refactored versions produce **identical results** to the originals

## Getting Started

1. Open `src/mystery_code.py`
2. Select a function and ask Copilot Chat: _"Explain what this function does"_
3. Create `src/clean_code.py` and rewrite each function with:
   - Descriptive variable names
   - Logical line breaks
   - Clear comments explaining the algorithm
   - Meaningful function/parameter names
4. Run the verification tests: `pytest tests/ -v`

## Expected End State

You should have:
- `src/clean_code.py` with three refactored functions that mirror the behavior of `mystery_code.py`
- All tests in `tests/test_equivalence.py` passing
- Each function should be readable enough that a junior developer could understand it

```bash
cd exercises/02-understand-code
pytest tests/ -v
```

## Hint

> Copilot excels at explaining code when you highlight specific sections and ask targeted questions. Try: "What algorithm is this implementing?" or "What are the edge cases in this logic?"

**One thing you'll need to figure out on your own:** The third function (`fn3`) uses a non-obvious optimization. When you refactor it, you'll need to understand *why* it works that way — a naive rewrite will be functionally correct but dramatically slower for large inputs. You'll need to ask Copilot the right question to understand the performance characteristic and preserve it in your refactored version.
