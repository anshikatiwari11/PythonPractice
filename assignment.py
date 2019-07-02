# How to reverse the function w/o using builtin function:
# a = "Hello World"[::-1]
# print(a)
# a = [1,2,3,4,5,6,7,8][::-1]
# print(a)
# How to append in a list in python w/o using append builtin function:
# a = [1,2,3]
# b = [4,5,6]
# a[:0] = b
# print(a)
# How to insert in list in python w/o using insert builtin function:
# a = [1,2,3]
# b = [4,5,6]
# a[1:0] = b
# print(a)
# How to extend list in the last in python w/o using extend builtin function:
# a = [1,2,3]
# b = ['x','y','z']
# a[3:0] = b
# print(a)

# How to sort in list in python without using sort builtin function
# a = [5, 3, 7, 2, 8, 4]
# print(a)
# n = len(a)
# for i in range(n):
#     for j in range(1, n-i):
#         if a[j-1] < a[j]:
#             (a[j-1], a[j]) = (a[j], a[j-1])
# print(a)

a = ['b','c','a','d']
# print(a)
# n = len(a)
# for i in range(n):
#     for j in range(1, n-i):
#         if a[j-1] < a[j]:
#             (a[j-1], a[j]) = (a[j], a[j-1])
# print(a)

# How to delete/clear in list in python without using sort builtin function
# a = [1,2,3,4,5,6,7,8]
# a= a[7:7]
# print(a)

# How to pop in list in python without using sort builtin function
# a = [1,2,3,4,5,6,7,8]
# a= a[0:7] or a= a[0:-1]
# print(a)

# How to copy in list in python without using sort builtin function
# a = [1,2,3,4,5,6,7,8]
# b = a
# print(b)
#fibnaci series
# def fib(n):
#     a,b=0,1
#     while a<n:
#         print(a,end=' ')
#         a,b = b, a+b
#     print()
# fib(1000)



# Making Shallow Copies: It creates a new object which stores the reference of the original elements.
# So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects.
# This means, a copy process does not recurse or create copies of nested objects itself.
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# y = list(x)
# print(x)
# print(y)
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# xx = ['anshika']
# x[2:0] = xx
# print(x)
# print(y)

# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# new_list = old_list
# new_list[2][2] = 9
# print('Old List:', old_list)
# print('ID of Old List:', id(old_list))
# print('New List:', new_list)
# print('ID of New List:', id(new_list))

# Making Deep Copies: A deep copy creates a new object
# and recursively adds the copies of nested objects present in the original elements.




