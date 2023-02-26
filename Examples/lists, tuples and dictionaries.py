# Lists. list_name = ["value", 1, 1.2, False] Ordered, Indexed and can be changed.

my_list = ["Banana", 17, 3.14159, True]
print(my_list[1])   # Prints 17
my_list.insert(1, "Boo")
print(my_list[1])   # Prints Boo (17 is now moved to index 2)
print()

# 2D Lists. list_two = [list_name, list_name_b, list_name_c] Ordered, Indexed and can be changed. List of lists.
my_list_b = ["Bread", 19, 4.2, False]

list_two = [my_list, my_list_b]
print(list_two[0][0])   # Prints Banana
print(list_two[1][0])   # Prints Bread
print()

# Tuples. tuple_name = ("Jack", 13, "male") Unordered, Unindexed and cannot be changed.
student = ("Jack", 13, "male")
if "male" in student:   # True
    print("True")   # Prints True
print()

# Dictionaries. dict_name = {"A": "1",
#                            "B": "2",
#                            "C": "3",
#                            "D": "4"}
# A, B, C and D are known as keys. 1, 2, 3 and 4 are the values corresponding to these keys.
capitals = {"UK": "London",
            "USA": "Washington DC",
            "India": "New Delhi",
            "Brazil": "Rio de Janeiro",
            "Nigeria": "Lagos"}
for key, value in capitals.items():
    print(key, value)   # Prints list of dictionary keys and their corresponding values
