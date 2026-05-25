# Exercise 3: Code Conversion (Python → Java)

## Objective

Learn how to **safely convert code** from one language to another using GitHub Copilot, with **test-driven validation** that the converted code is functionally identical.

## The Problem

Language conversion is one of Copilot's most impressive capabilities — but how do you **know** the converted code is correct? A function might look right but have subtle differences in:

- Integer overflow behavior
- Floating-point precision
- String handling (null vs empty)
- Collection mutability
- Exception semantics

The answer: **ensure comprehensive test coverage BEFORE converting**, then convert both the code AND the tests. If the converted tests pass, you have high confidence the conversion is correct.

## Your Task

The file `src/inventory_manager.py` contains a Python inventory management system with full test coverage in `tests/test_inventory.py`.

Your job:
1. Review the Python implementation and its tests
2. Verify all Python tests pass first
3. Use GitHub Copilot to convert `inventory_manager.py` → `src/InventoryManager.java`
4. Convert `test_inventory.py` → `src/InventoryManagerTest.java`
5. Run both test suites and confirm they all pass

## Getting Started

1. Open `src/inventory_manager.py` — understand the API
2. Run the Python tests to establish a baseline:
   ```bash
   cd exercises/03-code-conversion
   pytest tests/ -v
   ```
3. Open `src/inventory_manager.py` and ask Copilot to convert it to Java
4. Create `src/InventoryManager.java` with the converted code
5. Convert the tests to JUnit 5 in `src/InventoryManagerTest.java`
6. Compile and run the Java tests:
   ```bash
   cd src
   javac -cp .:junit-platform-console-standalone-1.10.0.jar InventoryManager.java InventoryManagerTest.java
   java -cp .:junit-platform-console-standalone-1.10.0.jar org.junit.platform.console.ConsoleLauncher --select-class InventoryManagerTest
   ```

## Expected End State

- All Python tests pass: `pytest tests/ -v` shows green
- Java files compile without errors
- All JUnit tests pass with equivalent assertions
- The Java implementation handles the same edge cases as Python

## Hint

> When converting, pay attention to how Python and Java differ in:
> - Dictionary/HashMap behavior with missing keys
> - Exception types (KeyError → appropriate Java exception)
> - Default parameter values (Python supports them, Java uses overloads)
> - List comprehensions → Stream API or loops

**One thing you'll need to figure out on your own:** The Python code uses a specific floating-point rounding strategy for price calculations. Java's default floating-point behavior differs subtly. You'll need to identify where this matters and ensure your Java conversion handles currency values the same way. Simply translating the code line-by-line won't produce identical results for all test cases.
