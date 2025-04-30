

# Reading Error Messages

# def find_first_nonzero_among(numbers):
#     for n in numbers:
#         if n != 0:
#             return n

# find_first_nonzero_among(0, 0, 1, 0, 2, 0)

# The error message tells you that the function find_first_nonzero_among was given 6 arguments b
# ut expects only 1

# The second function invocation (line 7) receives the correct number of arguments, 
# so no error is raised on line 1. However, as soon as the program tries to evaluate line 2 
# with the given argument, it raises another TypeError:

# find_first_nonzero_among(1)

# This is because the function parameter numbers is now bound to the provided argument 1, 
# so it tries to evaluate for n in numbers:. 
# Since integers are not iterables, this raises a TypeError.



# Weather Forecast

# import random

# def predict_weather():
#     sunshine = random.choice([True, False])

#     if sunshine:
#         print("Today's weather will be sunny!")
#     else:
#         print("Today's weather will be cloudy!")

# predict_weather()



# Multiply By Five

# Solution 1

# def multiply_by_five(n):
#     return n * 5

# print("Hello! Which number would you like to multiply by 5?")
# number = input()

# print(f"The result is {multiply_by_five(int(number))}!")


# # Solution 2 - Solution

# def multiply_by_five(n):
#     return n * 5

# print("Hello! Which number would you like to multiply by 5?")
# number = int(input())

# print(f"The result is {multiply_by_five(number)}!")



# Pets

# Solution 1

# pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

# pets['dog'] = ['bowser','sparky', 'fido']

# print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}


# Solution 2

# pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

# pets['dog'].append('bowser')

# print(pets)
# # {'cat': 'pepe',
# #  'dog': ['sparky', 'fido', 'bowser'],
# #  'fish': 'oscar'}



# Confucius Says

# Solution 1

# def get_quote(person):
#     if person == 'Yoda':
#         return 'Do. Or do not. There is no try.'
#     if person == 'Confucius':
#         return 'I hear and I forget. I see and I remember. I do and I understand.'
#     if person == 'Einstein':
#         return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'
    

# print('Confucius says:')
# print('"' + get_quote('Confucius') + '"')




# Populate List

# Solution 1

# numbers = []

# for i in range(1,6):

#     numbers.append(i)


# print(numbers)



# Dictionary Access

# Solution 1

# info = {'name': 'Srdjan', 'age': 38}

# print(info['city']) # KeyError: 'city'

# Solution 2

# info = {'name': 'Srdjan', 'age': 38}

# print(info.get('city', 'Unknown'))



# Matrix

# Solution 1

# sub_list = ["-", "-", "-"]
# matrix = []

# for i in range(3):
#     matrix.append(["-"] * 3)
    

# matrix[0][0] = "X"

# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# # Solution 2

# sub_list = ["-", "-", "-"]
# matrix = []

# for _ in range(3):
#     matrix.append(sub_list.copy())

# matrix[0][0] = "X"
# print(matrix) # [['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]



# Find Maximum

# Solution 1

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     max_number = float('-inf')
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     return max_number

# print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
# print(find_maximum([-1, 0, 5, 3]))         # Expected 5
# print(find_maximum([-10, -3, -20, -2]))   # Expected -2


# Digit Product

# Solution 1

# def digit_product(str_num):
#     digits = [int(n) for n in str_num]
#     product = 1

#     for digit in digits:
#         product *= digit

#     return product

# result = digit_product('12345')
# print(result)  # expected: 120, actual: 0
