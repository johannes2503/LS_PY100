# First Car

# car = {
#     'type' : 'sedan',
#     'color' : 'blue',
#     'milage' : 80_000,
# }



# Adding the year

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
# }

# car['year'] = 2003

# print(car)


# Brokken Odometer

# Solution 1

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
#     'year':    2003,
# }

# car.pop('mileage')
# print(car)

# Solution 2 - Solution

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
#     'year':    2003,
# }

# del car['mileage']
# print(car)


# What Color?

# Solution 1

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# print(car['color'])


# What's My Length?

# Solution 1

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# print(len(car))


# Checking Key Existence

student = {
    'id': 123,
    'grade': 'B',
}

# Solution 1

# if 'id' and 'grade' in student:
#     print('ID and Grade exists')
# else:
#     print('ID and Grade do not exist')

# Solution 2 - Solution

# print('name' in student)      # False
# print('grade' in student)     # True


# Multiple Cars

# Solution 1

# {
#     'car': {
#         'type':    'sedan',
#         'color':   'blue',
#         'year':    2003,
#     },
#     'truck': {
#         'type':    'pickup',
#         'color':   'red',
#         'year':    1998,
#     },
# }



# Which Collection?

# Solution 1

# car = [
#     ['type', 'sedan'],
#     ['color', 'blue'],
#     ['year', 2003],
# ]



# Divided by Two

# Solution 1

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }

# for value in numbers.values():
#     half_numbers = int(value / 2)
#     print(half_numbers)

# Solution 2 - Solution

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }

# half_numbers = []
# for value in numbers.values():
#     half_numbers.append(value // 2)

# print(half_numbers)



# Labeled Numbers

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    10,
# }

# Solution 1

# for key, value in numbers.items():
#     print(f'{key} number is: {value}')