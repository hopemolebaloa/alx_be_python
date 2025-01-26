import math

class Shape:
    """
    A base class representing a generic shape.
    """
    def area(self):
        """
        Abstract method to calculate the area of a shape.
        Should be overridden in derived classes.
        """
        raise NotImplementedError("The area method must be overridden in derived classes.")

class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        """
        Initializes a Rectangle instance with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        Formula: length × width
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        """
        Initializes a Circle instance with radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        Formula: π × radius²
        """
        return math.pi * self.radius ** 2
