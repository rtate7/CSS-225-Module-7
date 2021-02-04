# Bob Tate
# 2/4/21

# Problem 1: Area of Circle - returns the area of a circle of 
# radius r.

import math

def areaOfCircle(r):
    return math.pi * r ** 2

# def test_areaOfCircle(r, a):
#     try:
#         assert math.isclose(areaOfCircle(r), a, rel_tol=0.1)
#         print(f'Test passed for input ({r})')
#     except:
#         print(f'Test failed for input ({r})')

# test_areaOfCircle(0, 0)
# test_areaOfCircle(1, 3.14)
# test_areaOfCircle(5, 78.5)

print(f"The area of a circle with radius 5 is {areaOfCircle(5)}")
