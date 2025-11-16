"""Now that you can tell the difference between pure and impure functions, let’s try it out.

Create a pure function to calculate the area of a circle given its radius.

Define a calculate_circle_area() function that takes the radius of the circle as input.
Compute the area of the circle using the formula: area=π∗r**2.
Return the result."""



def calculate_circle_area(radius):
    from math import pi
    return pi*radius**2
print(calculate_circle_area(10))