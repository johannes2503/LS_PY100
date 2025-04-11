# PYTHON BASICS

# Length

# length = "These aren't the droids you're looking for."

# print(len(length))


# ALL CAPS

# string = 'confetti floating everywhere'

# print(string.upper())


# Ignoring Case

# Version 1

# name = 'Roger'

# name2 = 'RoGer'

# if name == name2:
#     print(True)
# else:
#     print(False)


# # Version 2 - Solution

# name = 'Roger'

# print(name.casefold() == 'RoGeR'.casefold())      # True
# print(name.casefold() == 'DAVE'.casefold())       # False


# Multiline String

# string = 'A pirate I was meant to be!\nTrim the sails and roam the sea!'
# string2 = '''A pirate I was meant to be!
# Trim the sails and roam the sea!'''
# print(string)
# print(string2)


# Contains Character

# char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

# if 'x' in char_sequence:
#     print(True)

# print('x' in char_sequence)

# def is_empty(a):
#     return a == ''


# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True


# Is Empty or Blank?

# def is_empty_or_blank(s):
#     return s.strip(' ') == ''


# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True


# Capitalize Words

# string = 'launch school tech & talk'

# print(string.title())


# Check Prefix

# Version 1

# def starts_with(s1, s2):
#     if s2 in s1:
#         return True
#     else:
#         return False

# Version 2 - Solution

# def starts_with(string, prefix):
#     return string.startswith(prefix)


# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True


# Count Substrings

def count_substrings(string, substring):
    s = string.count(substring)
    return s


print(count_substrings("lemon lemon lemon", "lemon"))  # 3
print(count_substrings("laLAlaLA", "la"))  # 2
print(count_substrings("launch", "uno"))  # 0
