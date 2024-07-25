# Simple Python program to calculate the area of a rectangle

def calculate_rectangle_area(length, width):
    # Calculate the area of the rectangle
    area = length * width
    return area

def main():
    # Prompt the user to enter the length of the rectangle
    length = float(input("Enter the length of the rectangle: "))
    
    # Prompt the user to enter the width of the rectangle
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate the area of the rectangle
    area = calculate_rectangle_area(length, width)
    
    # Print the area of the rectangle
    print(f"The area of the rectangle with length {length} and width {width} is {area} square units.")

if __name__ == "__main__":
    main()
