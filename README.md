# GitHub Copilot Workshop Series

Welcome! This workshop series contains three hands-on coding exercises designed to teach you how to get the most out of GitHub Copilot as an AI-powered coding assistant. These exercises go beyond simple code completion — they focus on the **prompting techniques** and **workflows** that separate a casual Copilot user from a power user.

Each exercise takes approximately **10–15 minutes** to complete with Copilot's assistance and is aimed at university students and recent graduates with a working knowledge of Python and/or Java.

---

## Prerequisites

Before you begin, make sure you have the following set up on your machine:

- **GitHub Copilot** enabled and active in your IDE (VS Code recommended)
- **Python 3.10+** installed and available on your PATH
- **Java 17+** installed (required for Exercise 3's conversion target)
- **pytest** installed in your Python environment (`pip install pytest`)

> **Tip:** If you're using a virtual environment (recommended), activate it before running any exercises:
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate   # macOS/Linux
> pip install pytest
> ```

---

## Exercises

This workshop consists of three progressively challenging exercises. You can complete them in any order, but they are designed to build on each other conceptually.

| # | Exercise | Language | What You'll Learn |
|---|----------|----------|-------------------|
| 1 | [Unit Test Generation](exercises/01-unit-test-generation/README.md) | Python | How to prompt Copilot to generate non-obvious edge-case tests — not just the happy path |
| 2 | [Understand Code](exercises/02-understand-code/README.md) | Python | How to use Copilot to explain obfuscated code and refactor it into clean, readable implementations |
| 3 | [Code Conversion](exercises/03-code-conversion/README.md) | Python → Java | How to safely convert code between languages and use test coverage as proof of correctness |

### Exercise Summaries

**Exercise 1 — Unit Test Generation:** You're given a working Python class with basic tests already written. Your challenge is to use Copilot to generate a comprehensive test suite that covers edge cases like timezone boundaries, leap years, and unusual date configurations. The key skill: learning that *how you describe the edge cases to Copilot* dramatically affects the quality of generated tests.

**Exercise 2 — Understand Code:** You're given three deliberately obfuscated Python functions with single-character variable names, no comments, and dense one-liners. Your challenge is to use Copilot to understand what each function does, then refactor them into clean, readable code — while preserving identical behavior (verified by tests).

**Exercise 3 — Code Conversion:** You're given a fully-tested Python inventory management system. Your challenge is to convert it to Java using Copilot, including converting the test suite. The key insight: if you convert the tests too and they all pass in Java, you have strong evidence the conversion is correct.

---

## Getting Started

1. **Clone this repository** to your local machine
2. **Set up your Python environment** (see Prerequisites above)
3. **Navigate to the exercise folder** you want to start with (e.g., `cd exercises/01-unit-test-generation`)
4. **Read the exercise README** — each one has detailed instructions, hints, and a description of the expected end state
5. **Use GitHub Copilot throughout** — Copilot Chat for explanations and planning, inline suggestions for implementation

---

## Tips for Success

- **Give Copilot context** — open the relevant files in your editor so Copilot can see the code you're working with
- **Use Copilot Chat** (`Ctrl+I` / `Cmd+I`) to ask targeted questions like "What algorithm is this?" or "What edge cases should I test?"
- **Iterate on your prompts** — if the first suggestion isn't great, rephrase your request with more specifics
- **Don't accept blindly** — always review generated code for correctness before moving on
- **Be specific about what you want** — vague prompts produce vague results; detailed prompts produce detailed results
