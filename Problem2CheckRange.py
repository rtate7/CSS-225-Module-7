# Bob Tate
# 2/4/21

# Problem 2: Checks whether a number is in a given range

def is_in_range(number, bottom, top):
    return number in range(bottom, top)

# def test_is_in_range(number, bottom, top, expected_value):
#     try:
#         assert is_in_range(number, bottom, top) == expected_value
#         print(f"Test passed for inputs number: {number}, bottom: {bottom}, top: {top}")
#     except:
#         print(f"Test failed for inputs number: {number}, bottom: {bottom}, top: {top}")

# test_is_in_range(5, 1, 10, True)
# test_is_in_range(11, 1, 10, False)
# test_is_in_range(0, 1, 10, False)
# test_is_in_range(10, 1, 10, False)
# test_is_in_range(1, 1, 10, True)

print(f"5 is in range 1 - 10: {is_in_range(5, 1, 10)}")
print(f"0 is in range 1 - 10: {is_in_range(0, 1, 10)}")
