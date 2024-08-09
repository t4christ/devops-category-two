# Tuples are similar to list with the only difference is that they are immutable
# my_tuple = ('apple', 'banana', 'cherry')
# print(my_tuple[2]) # cherry

#Altough tuples are immutable, we can change them to List make changes and then change back to Tuples
my_tuple = ("apple", "banana", "cherry")
y = list(my_tuple)
y[1] = "kiwi"
my_tuple = tuple(y)

print(my_tuple)  # Output: ('apple', 'kiwi', 'cherry')