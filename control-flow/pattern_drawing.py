# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through each row
row = 0
while row < size:
    # Use a for loop to print asterisks for each column in the row
    for col in range(size):
        print("*", end="")
    # Print a newline character after each row
    print()
    row += 1
