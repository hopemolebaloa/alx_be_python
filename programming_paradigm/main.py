import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command line interaction for the division calculator.
    """
    # Ensure exactly two arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Get the numerator and denominator from command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform safe division
    result = safe_divide(numerator, denominator)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
