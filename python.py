import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of a circle with radius {radius} is {area:.2f}")

if __name__ == "__main__":
    main()
