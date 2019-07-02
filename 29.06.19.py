# Inner Class: Means Class inside class

# class student:
#     def __init__(self,r,n):
#         self.rollno = r
#         self.name = n
#         self.lap = self.Laptop()
#         self.student_detail()
#     def student_detail(self):
#         print('Student name is {} and Roll no is {} and Laptop Configuration is {}'.format(self.rollno,self.name, self.lap.configure()))
#     class Laptop():
#         def __init__(self):
#             self.ram = '4 GB'
#             self.rom = '160 GB'
#             self.disc_type = 'SATA'
#         def configure(self):
#             return "ram is {}".format(self.ram)
# s= student(5,"Anshika")

# class student:
#     def __init__(self,r,n):
#         self.rollno = r
#         self.name = n
#         self.lap = self.Laptop()
#         self.student_detail()
#     def student_detail(self):
#         print('Student name is {} and Roll no is {} and Laptop Configuration has {}'.format(self.rollno,self.name, self.lap.configure()))
#     class Laptop():
#         def __init__(self):
#             self.ram = '4 GB'
#             self.rom = '160 GB'
#             self.disc_type = 'SATA'
#         def configure(self):
#             return "RAM is {} and ROM is {} and Disc_type is {}".format(self.ram,self.rom, self.disc_type)
# s= student(5,"Anshika")

# Single level inheritance:
# class Parent():
#     def f3(self):
#         print("I am in f3")
# class Child(Parent):
#     def f1(self):
#         print("I am in f1")
#     def f2(self):
#         print("I am in f2")
# c= Child()
# c.f3()


# Multi Level Inheritance:
# class GreatGrandParent():
#     def f3(self):
#         print("f3")
# class GrandParent(GreatGrandParent):
#     def f2(self):
#         print("f2")
# class Parent(GrandParent):
#     def f1(self):
#         print("f1")
# class Child(Parent):
#     def f0(self):
#         print("f0")
# c= Child()
# c.f0()

# Multiple Inheritance:
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
# print(D.__mro__)

# MRO C3 Algorithm:
# class D:
#     pass
# class A(D):
#     pass
# class B(D):
#     pass
# class C(D):
#     pass
# class X(A,B):
#     pass
# class Y(B,C):
#     pass
# class Z(X,Y,C):
#     pass
# print(Z.__mro__)






