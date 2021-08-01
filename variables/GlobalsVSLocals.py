# global keyword  is used to modify a variable
# outside of the current scope.
def change_global():
    global count_global
    count_local = 2
    count_global += count_local
    print(count_global)


count_global = 10
change_global()
