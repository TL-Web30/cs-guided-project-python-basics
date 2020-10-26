"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
    # Your code here
    #check to make sure txt will make sense as an integer
    #use isnumeric function
    if str.isnumeric(txt) is True:
        converted = int(txt)
        return converted
    else:
        return f"'{txt}' is not a valid number"


print(string_int("6"))
print(string_int("1000"))
print(string_int("12"))
print(string_int("hi"))

