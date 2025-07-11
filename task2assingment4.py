# Step 1: Take user input and write to output.txt
user_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data to the same file
additional_input = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
