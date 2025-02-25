import math

def greet(name):
    """Returns a greeting message"""
    return f"Hello, {name}! Welcome to Python modules."

def calculate_square(number):
    """Returns the square of a number"""
    return number ** 2

class MathOperations:
    """A class for basic math operations"""
    def __init__(self):
        self.pi = math.pi  # Using math module already imported
        
    def circle_area(self, radius):
        """Calculate the area of a circle"""
        return self.pi * radius ** 2
