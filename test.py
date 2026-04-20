try:
    input = int(input("Enter a digit: "))
except ValueError:
    print("Invalid input. Please enter a valid digit.")
    input = int(input("Enter a digit: "))