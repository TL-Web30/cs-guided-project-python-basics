"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    # Your code here
    #figure out the number of o's and x's
    #check if the number is same, return true if are
    #return false if not
    #how to keep track of numbers of x's and o's
    # we can keep two counters, one for x and one for o
    x_count = 0
    o_count = 0
    for letter in txt:
        if letter.lower() == 'x':
            x_count += 1
        if letter.lower() == 'o':
            o_count += 1

    if x_count == o_count:
        return True
    else:
        return False

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))

