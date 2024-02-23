#!/usr/bin/python3
""" 
A list is a python built in-built type. Its a sequence of comma separated
    items, enclosed in square brackets(ordered)
A list is mutable, items can be modified and accessed using there index
'+' - Concatenation
'*' - repetition
"""

list1 = ["Brian", 21, "Omondi", 00]
list2 = ["Eddy", 16, "Otieno", 10]

""" Access List items """
obj1 = list1[0] #Brian
obj = list2[3]
ob3 = list1 + list2
print(ob3[5])
print(obj1, obj)

""" List operations """
# Repetition
a = ['Hi!'] * 4
print(a)

#Concatenation
b = [1, 2, 3] + [4, 5, 6]
print(b)

# membership
3 in [1, 3, 5]

# Operations continued
""" When slicing:
    a = list[i:j]
        where: i -> first item in the sublist
                j -> index of item next to the last in the sublist
"""
sublist = list1[0:3]
print(sublist)

#Lists immutability
""" Adding items
    list[i]=newvalue
    
"""
list3 = [1, 2, 3, 4]
list3[3] = 10
print(list3)


