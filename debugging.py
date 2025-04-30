

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

import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")