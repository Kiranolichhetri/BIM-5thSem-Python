# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
radius = 5
circle = Circle(radius)

print(f"Radius of the circle: {radius}")
print(f"Area of the circle: {circle.area():.2f}")
print(f"Perimeter of the circle: {circle.perimeter():.2f}")
