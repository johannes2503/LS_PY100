# PYTHON BASICS

# Functions

# Multiply

# def multiply(a, b):
#     print(a * b)


# multiply(12, 4)

# Print Quote

# def bruce_eckel_quote():
#     print('Python is executable pseudocode.')


# bruce_eckel_quote()

# Cite the Author

# def cite(str1, str2):
#     print(f'{str1} said: {str2}')


# cite('Bruce Eckel', 'Python is executable pseudocode.')

# Squared Number

# def squared_number(num):
#     return num ** 2


# squared_number(3)

# Display Divison

# def multiples_of_three():
#     divisor = 1

#     for dividend in range(3, 31, 3):
#         print(f'{dividend} / {divisor} = 3')
#         divisor += 1


# multiples_of_three()

# Three-way Comparison

#  Version 1

# def compare_by_length(str1, str2):
#     if len(str1) < len(str2):
#         print(-1)
#     elif len(str1) > len(str2):
#         print(1)
#     elif len(str1) == len(str2):
#         print(0)

# Version 2 - solution

# def compare_by_length(str1, str2):
#     if len(str1) < len(str2):
#         return -1
#     elif len(str1) > len(str2):
#         return 1
#     else:
#         return 0


# # compare_by_length('patience', 'perseverance')
# # ccompare_by_length('strength', 'dignity')
# compare_by_length('humor', 'grace')

# Transformation

# string = 'Captain Ruby'

# new_string = string.replace('Ruby', 'Python')

# print(new_string)

# Internationalization 1

# def greet(lang):
#     match lang:
#         case 'en':
#             print('Hi!')
#         case 'fr':
#             print('Salut!')
#         case 'pt':
#             print('Olá!')
#         case 'de':
#             print('Hallo!')
#         case 'sv':
#             print('Hej!')
#         case 'af':
#             print('Haai!')


# greet('fr')         # Hi!
# print(greet('fr'))         # Salut!
# print(greet('pt'))         # Olá!
# print(greet('de'))         # Hallo!
# print(greet('sv'))         # Hej!
# print(greet('af'))         # Haai!

# Locale Part 1

# def extract_language(locale):
#     return locale.split('_')[0]


# print(extract_language('en_US.UTF-8'))      # en
# print(extract_language('en_GB.UTF-8'))      # en
# print(extract_language('ko_KR.UTF-16'))     # ko

# Locale Part 2

# Version 1

# def extract_region(locale):
#     return locale[3:5]


# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR

# # Version 2 - Solution

# def extract_region(locale):
#     return locale.split('.')[0].split('_')[1]


# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR

# Internationalization 2

# Version 1

# def local_greet(locale):
#     lang_in_str = locale.split('.')[0]

#     if 'en_US' in lang_in_str:
#         return 'Hey!'
#     elif 'en_GB' in lang_in_str:
#         return 'Hello!'
#     elif 'en_AU' in lang_in_str:
#         return 'Howdy!'


# print(local_greet('en_US.UTF-8'))      # Hey!
# print(local_greet('en_GB.UTF-8'))       # Hello!
# print(local_greet('en_AU.UTF-8'))       # Howdy!

# Version 2 - Solution

# def greet(language_code):
#     match language_code:
#         case 'en':
#             return 'Hi!'
#         case 'fr':
#             return 'Salut!'
#         case 'pt':
#             return 'Olá!'
#         case 'de':
#             return 'Hallo!'
#         case 'sv':
#             return 'Hej!'
#         case 'af':
#             return 'Haai!'

# def extract_language(locale):
#     return locale.split('_')[0]

# def extract_region(locale):
#     return locale.split('.')[0].split('_')[1]

# def local_greet(locale):
#     language = extract_language(locale)
#     region = extract_region(locale)

#     match (language, region):
#         case ('en', 'US'):
#             return 'Hey!'
#         case ('en', 'GB'):
#             return 'Hello!'
#         case ('en', 'AU'):
#             return 'Howdy!'
#         case _:
#             return greet(language)


# print(local_greet('en_US.UTF-8'))      # Hey!
# print(local_greet('en_GB.UTF-8'))       # Hello!
# print(local_greet('en_AU.UTF-8'))       # Howdy!
