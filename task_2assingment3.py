import math

def main():
    # 1. Ask the user for a number as input
    num_str = input("Enter a positive number: ")
    try:
        number = float(num_str)
        if number <= 0:
            raise ValueError("Number must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # 2. Calculate using math module
    sqrt_val = math.sqrt(number)
    log_val = math.log(number)        # natural logarithm (base e)
    sine_val = math.sin(number)       # sine of the number in radians

    # 3. Display the results
    print(f"Square root of {number} is {sqrt_val:.4f}")
    print(f"Natural logarithm of {number} is {log_val:.4f}")
    print(f"Sine of {number} (in radians) is {sine_val:.4f}")

if __name__ == "__main__":
    main()
