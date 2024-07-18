def factorial(n):
    """Function to calculate the factorial of a number"""
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

def main():
    # Ask the user for input
    num = int(input("Enter a number to calculate its factorial: "))

    # Calculate factorial
    result = factorial(num)

    # Print the factorial
    print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
