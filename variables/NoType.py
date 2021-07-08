# Python is NOT strictly typed.
# So no need to declare the type.
# And also can be re-declared.
name = "Smart Program"
age = 22
age = "Smart Program"
name = 22

def printdata():
    # age int value needs to be converted to str.
    print("Name \t: " + age + "\n" + "Age \t: " + str(name))


printdata()
