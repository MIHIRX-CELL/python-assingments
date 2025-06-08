'''
# even_odd_parentheses.py

def is_even(num):
    return num % 2 == 0

def main():
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Error: enter a valid integer.")
        return

    if is_even(num):
        print(str(num) + " is Even")
    else:
        print(str(num) + " is Odd")

    print("Thank you!")

if __name__ == "__main__":
    main()
