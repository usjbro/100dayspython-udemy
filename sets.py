# sets are unordered lists
numbers = [1, 1, 2, 3, 4]
print(f"Numbers: {numbers}")
first = set(numbers)
print(f"First set: {first}")
second = {1, 4}
print(f"Second Set: {second}")
second.add(5)
print(f"5 added to second: {second}")
second.remove(5)
print(f"5 removed from second: {second}")
second_len = len(second)
print(f"Length of second: {second_len}")
#a new set that contains all the elements which are present in either of the original sets
third = first | second
print(f"Union of first and second {third}")
# a new set that contains only the elements which are common to both of the original sets
third = first & second
print(f"Intersection of first and second {third}")
# a new set containing elements that are present in the first set but not in the second set
third = first - second
print(f"Difference of first and second {third}")
# the symmetric difference collection of elements that are in either set, but not in both
third = first ^ second
print(f"Symmertic Difference of first and second {third}")