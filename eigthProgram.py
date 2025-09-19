# data structures
# four types of data structures
# Tuples, Dictionaries, List, Set in python


# List - []
# keywords are - Mutable, Duplicates, Ordered, Heterogenous
# Mutable - value can be changed after creation
# Duplicates - same value occuring multiple time, List allows this
# Ordered - you can access elements using their position
# Heterogenous - we can have multiple data types inside the List

# [10, False ,11, 18.5, 12, 13, "two" , 14, 15, 12, 60, 10, "One", True, print()] example

# print Amit from this listing
# a = [12, 16, "Amit", True, 18.4]
# print(a[2])
# print(a[-3])
# # print 12, 16, "Amit"
# print(a[0:3])

# 1 way to print all
# for i in range(len(a)):
#     print(a[i])

# 2 way to print all
# for i in a:
#     print(i)

# l = [1, 2, 3]
# l.append(4)
# l.append(5)
# print(l)

# print positive and negative elements of list
# k = [-45, 67, 78, -42, 33, 56,-23]
# print("positive element are ")
# for i in k:
#     if i >= 0:
#         print(i)
# print("Negative elements are")
# for i in k:
#     if i < 0:
#         print(i)


# find greatest value
# value = [12, 34, 24, 145, 234, 543, 45]

# largest = value[0]
# index = 0

# for i in range(len(value)):
#     if value[i] > largest:
#         largest = value[i]
#         index = i

# print(f"Largest value is {largest} at index {index}")

# find the second largest number
# value = [12, 34, 24, 145, 234, 543, 45, 236]
# largest = value[0]
# sec_largest = value[0]
# for i in value:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(f"first largest value {largest} and second is {sec_largest}")


# check list sorted or mot

# sorted = [12, 13, 14, 15, 16, 17]
# for i in range(len(sorted)-1):
#     if sorted[i] < sorted[i+1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break
# else:
#     print("your list is sorted")