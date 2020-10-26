"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # Your code here
    #takes a list, sorts so that the shortest string comes first
    #we need to know the length of each of the items in the array
    #there is a .sort method on lists in Python lst.sort()
    #.sort is alphabetical, not by length
    # we need to tell .sort method that we want to sort by length, by adding in the key
    #which we will use the length as the key
    #return sorted output
    lst.sort(key=len)
    return lst


print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["may", "april", "september", "august"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
print(sort_by_length(["apple", "pie", "eye", "shortcake"]))
print(sort_by_length([]))

