# Bob Tate
# 2/4/21

# Problem 4: takes a list of numbers and returns a new list with
# unique elements of the first list.

def remove_duplicates(input_list):
    # return list(set(input_list))
    return_list = []
    for number in input_list:
        if number not in return_list:
            return_list.append(number)
    return return_list

input_list = [1, 3, 3, 3, 6, 2, 3, 5]
print(f"The list of unique numbers in the list {input_list} is {remove_duplicates(input_list)}.")
