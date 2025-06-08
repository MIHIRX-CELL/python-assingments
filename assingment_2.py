# sum_1_to_50_list.py

def main():
    nums = [i for i in range(1, 51)]  # uses [ ] to store all numbers
    total = 0
    for i in nums:
        total += i
    print("Sum from 1 to 50 is:", total)

if __name__ == "__main__":
    main()
