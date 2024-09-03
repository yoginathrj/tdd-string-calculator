
# String Calculator Project

## Overview

This project contains a `string_calculator` function that performs arithmetic operations on numbers provided as a string input. The function supports different delimiters and handles edge cases such as negative numbers.

## Requirements

- Python 3.x
- `unittest` (included in the standard Python library)

## Project Structure

```
.
├── string_calculator/
│   ├── __init__.py
│   ├── string_calculator.py
├── tests/
│   ├── __init__.py
│   ├── test_string_calculator.py
└── README.md
```

- `string_calculator/`: Directory containing the main function implementation.
- `tests/`: Directory containing unit tests for the `string_calculator` function.

## Running Unit Tests

To run the unit tests for the `string_calculator` function, follow these steps:

### 1. Clone the repository https://github.com/yoginathrj/tdd-string-calculator.git

### 2. Navigate to the Project Root Directory i.e. tdd-string-calculator

Make sure you are in the root directory of the project where the `tests` folder is located.

### 3. Run the Tests

You can run the tests using Python's built-in `unittest` module. Use the following command:

```bash
python -m unittest discover -s tests
```

This command will:

- Discover all the test files in the `tests` directory.
- Execute each test case defined in the `TestStringCalculator` class.

### 4. Verify the Output

If all tests pass, you will see an output like this:

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

If any test fails, the output will display details of the failure.
