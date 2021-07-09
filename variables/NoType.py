# Python is NOT strictly typed.
# So no need to declare the variable type.
# Also variables can be re-declared.
_name = "Smart Program"
age = 22
age = "Smart Program"
_name = 22

def print_data():
    # age int value needs to be converted to str.
    print("Name \t: " + age + "\n" + "Age \t: " + str(_name))


print_data()
