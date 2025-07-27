def calculate_area(radius):
    """Calculate and return the area of a circle."""
    import math
    return math.pi * radius ** 2
# Example usage
if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area(radius)
    print(f"The area of the circle is: {area}")

def calculate_rectangle_area(length, width):
    """Calculate and return the area of a rectangle."""
    return length * width
# Example usage
if __name__ == "__main__":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
def add_two_numbers(num1, num2):
    """Add two numbers and return the result."""
    return num1 + num2