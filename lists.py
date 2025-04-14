# PYTHON BASICS


# First Element

# Version 1

# def first(list):
#     return list[0]

# # Version 2 - Solution

# def first(lst):
#     if lst:
#         return lst[0]
#     else:
#        return None


# print(first(['Earth', 'Moon', 'Mars']))  # Earth


# # Last Element


# ## Version 1

# def last(lst):
#     return lst[-1]

## Version 2 - Solution

# def last(lst):
#     if lst:
#         return lst[-1]
#     else:
#         return None


# print(last(['Earth', 'Moon', 'Mars']))

# # Add + Delete

# Version 1

# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# def add():
#     energy.append('geothermal')
#     energy.remove('fossil')
#     return energy

# print(energy)


# Alphabet


# Version 1

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# split = list(alphabet)

# print(split)

# Version 2 - Solution

# print(list(alphabet))


# Filter


# Version 1 - Solution

# scores = [96, 47, 113, 89, 100, 102]

# count = 0

# for score in scores:
#     if score >= 100:
#         count += 1

# print(count)


# Vocabulary

# Version 1

# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# for vocab in vocabulary:
#     for vocab2 in vocab:
#         print(vocab2)


# # happy
# # cheerful
# # merry
# # glad
# # tired
# # sleepy
# # etc...


# Equality

# Version 1

# list1 = [2, 6, 4]
# list2 = [2, 6, 4]

# print(list1 == list2)



# Type

# Version 1

# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'

# print(type(some_value1) is list)
# print(type(some_value2) is list)


# Version 2 - Solution

# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'

# isinstance(some_value1, list)  # True
# isinstance(some_value2, list)  # False



# Travel 

# Version 1

# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']

# def contains(city, destinations):
#     if 'Nashville' in city:
#         print(True)
#     else:
#         print(False)
    
# Version 2 - Solution

# def contains(element, destination):
#     for item in destination:
#         if item == element:
#             return True

#     return False
    

# contains('Barcelona', destinations)  # True
# contains('Nashville', destinations)  # False



# Passcode

# Version 1

# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# # Write some code here.
# # Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

# print('-'.join(passcode))



# Checking items off the grocery list

# Version 1 

# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']

# Your code.
# def items_off():
#     for i in range(len(grocery_list)):
#         del grocery_list[-1]
#         print(grocery_list)
               

# items_off()

# Version 2 - Solution

# while grocery_list:
#     checked_item = grocery_list.pop(0)
#     print(checked_item)