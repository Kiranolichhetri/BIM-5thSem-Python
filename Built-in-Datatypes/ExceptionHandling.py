def main():
    try:
        # Get user input
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Attempt the division
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

if __name__ == "__main__":
    main()
