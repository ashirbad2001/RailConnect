"""Simple command-line calculator.

Supports addition, subtraction, multiplication, and division.
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main() -> None:
    print("Simple Calculator")
    print("Choose operation: +  -  *  /")

    operator = input("Enter operator: ").strip()
    if operator not in {"+", "-", "*", "/"}:
        print("Invalid operator.")
        return

    try:
        first = float(input("Enter first number: ").strip())
        second = float(input("Enter second number: ").strip())

        if operator == "+":
            result = add(first, second)
        elif operator == "-":
            result = subtract(first, second)
        elif operator == "*":
            result = multiply(first, second)
        else:
            result = divide(first, second)

        print(f"Result: {first} {operator} {second} = {result}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
