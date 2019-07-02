
#fd= open(filename, mode)
# fd=open("d:\\python.txt", "r")
# print(fd.read())

#for printing the content in the line or line by line:
# fd=open("d:\\python.txt", "r")
# fd.seek(0)
# for line in fd.readlines():
#     print(line)

# fd=open("d:\\python.txt", "r")
# fd.seek(0)
# for line in fd.readlines():
#     if 'Class' in line:
#         print(line)
#     else:
#         print(not line)

# insert at starting in txt file:
# fd=open("d:\\python.txt", "a")
# fd.write("\n1234567")
# append
# fd=open("d:\\python.txt", "a")
# fd.write('Hello')
# append with space
# fd=open("d:\\python.txt", "a")
# fd.write(' Hello')
# fd=open("d:\\python.txt", "a")
# fd.write('*123*')
# print(fd)

# Console Work:
# 0 / 9
# 0.0
# try:
#     9 / 0
# except ZeroDivisionError as e:
#     print(e)
#
# division
# by
# zero
# try:
#     9 / 0
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     15 / 2
#
# division
# by
# zero
# try:
#     9 / 0
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print(15 / 2)
#
# division
# by
# zero
# 7.5
# try:
#     9 / 0
# except FileNotFoundError as e:
#     print("FileNotFoundError")
# except IndexError as e:
#     print("IndexError")
# except Exception as e:
#     print("Some Error")
# print(15 / 2)
# Some
# Error
# 7.5

# class student():
#     def __init__(self,n,r):
#         self.name = n
#         self.roll = r
#     def studentdetail(self):
#         print('student name is {} and roll is {}'.format(self.name,self.roll))
# s1=student('Anshika','5')
# s1.studentdetail()


# class student():
#      def __init__(self,n,r,sub):
#          self.name = n
#          self.roll = r
#      def studentdetail(self):
#          print('student name is {} and roll is {}'.format(self.name,self.roll))
#  s1=student('Anshika','5')
#  s1.studentdetail()


# class student():
#     def __init__(self, n, r, sub):
#         self.name = n
#         self.roll = r
#         self.subject = sub
#     def studentdetail(self):
#         print('student name is {} and roll is {}'.format(self.name, self.roll))
#     def calculate_percent(self):
#         sum = 0
#         for v in self.subject.values():
#             sum += v
#         print("Total precent is {}".format(sum * 100 / (len(self.subject.values()) * 100)))
#
# sub = {'Maths': 90, 'Physics': 92, 'Chemistry': 95, 'English': 87, 'Hindi': 78}
# s1 = student('Anshika', 5,sub)
# s1.studentdetail()
# s1.calculate_percent()

# Class Variable:
# class student():
#     school_name = "entral"
#     def __init__(self, n, r, sub):
#         self.name = n
#         self.roll = r
#         self.subject = sub
#     def studentdetail(self):
#         print('student name is {} and roll is {}'.format(self.name, self.roll))
#     def calculate_percent(self):
#         sum = 0
#         for v in self.subject.values():
#             sum += v
#         print("Total precent is {}".format(sum * 100 / (len(self.subject.values()) * 100)))
#
# sub = {'Maths': 90, 'Physics': 92, 'Chemistry': 95, 'English': 87, 'Hindi': 78}
# s1 = student('Anshika', 5,sub)
# s1.studentdetail()
# s1.calculate_percent()
# print(student.school_name)




# class student():
#     school_name = "entral"
#     def __init__(self, n, r, sub,address, mobilenumber):
#         self.name = n
#         self.roll = r
#         self.subject = sub
#         self._address = address
#         self.__mobile_number = mobilenumber
#     def studentdetail(self):
#         print('student name is {} and roll is {}'.format(self.name, self.roll))
#     def calculate_percent(self):
#         sum = 0
#         for v in self.subject.values():
#             sum += v
#         print("Total precent is {}".format(sum * 100 / (len(self.subject.values()) * 100)))
#
# sub = {'Maths': 90, 'Physics': 92, 'Chemistry': 95, 'English': 87, 'Hindi': 78}
# s1 = student('Anshika', 5,sub,'809',"0273867")
# print(s1._address)
# print(s1._student__mobile_number)

# class student():
#     @classmethod
#     def school_name(cls):
#         print(cls.school_name)
#     def calculate_percent(self):
#         sum = 0
#         for v in self.subject.values():
#             sum += v
#         print("Total precent is {}".format(sum * 100 / (len(self.subject.values()) * 100)))
#
# sub = {'Maths': 90, 'Physics': 92, 'Chemistry': 95, 'English': 87, 'Hindi': 78}
# s1 = student('Anshika', 5,sub,'809',"0273867")
# s1.schoolname()
