# Strings are arrays in python.
def print_string(some_text):
    print('Whole string is : ' + some_text)


def print_first_char(some_msg):
    print('First character of the string is : ' + some_msg[0])


def print_all_chars(some_str):
    print('All characters :', end=' ')
    for char in some_str:
        print(char, end=' ')
    print()


def print_chars_count(same_str):
    print('Number of Characters :', end=' ')
    print(len(same_str))


msg = 'This is an array of characters'
print_string(msg)
print_first_char(msg)
print_all_chars(msg)
print_chars_count(msg)
