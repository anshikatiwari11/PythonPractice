#Polymorphism
# 1.Ducktyping:

# class Laptop:
#     def code(self,ide):
#         ide.execute()
# class Pycharm:
#     def execute(self):
#         print("Pycharm: spell check")
#         print("Pycharm: follows pep8 standard")
#         print("Pycharm: compile and run")
# class Eclipse:
#     def execute(self):
#         print("Eclipse: compile and run")
# class Subline:
#     def execute(self):
#         print("Subline: only spell check")
# l1= Laptop()
# p1= Pycharm()
# 11.code(p1)

# 2. Operator Overloading:
# class student:
#     def __init__(self,p,c,m):
#         self.p = p
#         self.c = c
#         self.m = m
#     def __add__(self, other):
#         p1 = self.p + other.p
#         c1 = self.c + other.c
#         m1 = self.m + other.m
#         return student(p1,c1,m1)
# s1= student(32,43,54)
# s2= student(45,23,56)
# s3= s1 + s2
# print(s3.p)
# print(s3.c)
# print(s3.m)

# 3. Method Overloading: Not use in Python

# Default Parameter:
# def sum(a,b):
#     return a+b
# print(sum(5,6))

# if 3 parameters were there then,
# def sum(a,b,c=None):
#     return a+b+c
# print(sum(5,6))

# def sum(a,b,c=False):
#     return a+b+c
# print(sum(5,6))

# def sum(a,b,c=False):
#     return a+b+c
# print(sum(5,6,100))

# *Variable: Tuple
# def sum(*args):
#     for item in args:
#         print(item)
# sum(2,3,4,5,3,2,1,5)

# **Variable: Dictionary
# def sum(*args, **kwargs):
#     for item in args:
#         print(item)
#     print(kwargs)
# sum(2,3,4,5,3,2,1,5, a=5, b=4, c=7)

# Regular Expression:




