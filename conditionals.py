# PYTHON BASICS

# Conditionals

# Yes? No? Part1

# import random
# random_number = random.randint(0, 1)

# if random_number == 1:
#     print('Yes!')
# else:
#     print('No')

# Yes? No? Part2

# print('Yes!' if random_number else 'No')

# Check the Weather, Part 1

# weather = 'rainy'

# if 'sunny' in weather:
#     print('It\'s a beautiful day!')
# elif 'rainy' in weather:
#     print('Grab your umbrella')
# else:
#     print('Let\'s stay inside')

# Match-Case

# animal = 'horse'

# match animal:
#     case 'duck':
#         print('quack')
#     case 'squirrel':
#         print('nook nook')
#     case 'horse':
#         print('neigh')
#     case 'bird':
#         print('tweet tweet')
#     case _:
#         print('*cricket*')

# Check the Weather, Part 2

# weather = ''

# match weather:
#     case 'sunny':
#         print('It\'s a beautiful day!')
#     case 'rainy':
#         print('Grab your umbrella')
#     case _:
#         print('Let\'s stay inside')

# Logical Conditions 1

# if False or True:
#     print('Yes!')
# else:
#     print('No...')


# Logical Conditions 2

# if True and False:
#     print('Yes!')
# else:
#     print('No...')

# Logical Conditions 3

# sale = True
# admission_price = 5.25 if not sale else 3.99

# print(f"${admission_price}")

# Are we moving?

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)
