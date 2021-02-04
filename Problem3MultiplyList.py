# Bob Tate
# 2/4/21

# Problem 3: Multiplies all numbers in a list

def list_multiply(list):
    result = 1
    for number in list:
        result *= number
    return result

# def test_list_multiply(list, expected):
#     try:
#         assert list_multiply(list) == expected 
#         print(f"Test passed for input {list}")
#     except:
#         print(f"Test failed for input {list}")

# test_list_multiply([5,2,7,-1], -70)

input_list = [5, 2, 7, -1]
print(f"The result of multiplying all numbers in the list {input_list} is {list_multiply(input_list)}.")