from math_operations import greet, calculate_square, MathOperations


print(greet("Programmer"))
print(f"Square of 5: {calculate_square(5)}")

math_ops = MathOperations()
print(f"Area of circle with radius 3: {math_ops.circle_area(3):.2f}")