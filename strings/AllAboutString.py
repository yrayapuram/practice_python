# All about strings in python.
# Coding Style Tip: Function names should be lowercase,
# with words separated by underscores as necessary to improve readability.
def print_in_upper(some_str):
    print(some_str.upper())


def print_in_lower(some_str):
    print(some_str.lower())


def print_in_title(some_str):
    print(some_str.title())


# Returns index.
def find_char(some_str):
    print(some_str.find('S'))


def replace_word(some_str):
    print(some_str.replace('All', 'Everything'))


# Returns True OR False.
def find_word(some_str):
    if 'About' in some_str:
        print('Found word', end=': ')
    print('All' in some_str)


msg = 'All About Strings'
print_in_upper(msg)
print_in_lower(msg)
print_in_title(msg)
find_char(msg)
replace_word(msg)
find_word(msg)
print('Original String : ' + msg)
