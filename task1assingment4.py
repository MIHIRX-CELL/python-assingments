try:
    # Open the file in read mode
    with open("file.txt", "r") as file:
        # Read and print each line
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

