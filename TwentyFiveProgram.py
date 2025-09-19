# map, filter and zip

# map is used to applying a function to multiple items. It take a list or any sequences

# x = [1,2,3,4,5,6]
# result = map(lambda a : a * 2, x)
# # print(result) # this is a object now we convert in list for data
# print(list(result))


# filter -> as the name suggest is used to filter out the stuff. Takes a list or other sequences. Checks each item using a function (a test). Keeps only the items that pass the test.

# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# a = [2,3,5,6,8,10,11,12]
# result = filter(even, a)
# print(list(result))

# using lambda function

# a = [2,3,5,6,8,10,11,12]
# result = filter(lambda x : True if x % 2 == 0 else False, a)
# print(list(result))