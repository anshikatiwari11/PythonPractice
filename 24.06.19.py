# thisdict =	{"brand": "Ford", "model": "Mustang", "year": 1964}
# print(thisdict)
# x= thisdict.get("model")
# print(x)
# thisdict["year"] = 2019
# print(thisdict)
# for x in thisdict:
#   print(x)
# for x in thisdict:
#   print(thisdict[x])
# for x in thisdict.values():
#     print(x)
# for x in thisdict.keys():
#     print(x)
# for x, y in thisdict.items():
#   print(x, y)
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
# print(len(thisdict))
# thisdict["color"] = "red"
# print(thisdict)
# thisdict.pop("model")
# print(thisdict)
# mydict = thisdict.copy()
# print(mydict)
# mydict = dict(thisdict)
# print(mydict)

# a={1:"A",2:"B",3:"C"}
# for i,j in a.items():
#     print(i,j,end=" ")



# Homework
# Num = float(input("Enter the Number: "))
# if Num>0:
#     print("Positive Number")
# elif Num==0:
#     print("Zero")
# else:
#     print("Negative Number")



# Num1 = int(input("Enter the 1st number: "))
# Num2 = int(input("Enter the 2nd number: "))
# Num3 = int(input("Enter the 3rd number: "))
# if Num1>Num2 and Num1>Num3:
#     print("Num1 is greatest")
# elif Num2>Num1 and Num2>Num3:
#     print("Num2 is greatest")
# else:
#     ("Num3 is greatest")



# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# choice = input("Enter choice(1/2/3/4): ")
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if choice == "1":
#     print(num1,"+",num2,"=", add(num1,num2))
# elif choice == '2':
#    print(num1,"-",num2,"=", subtract(num1,num2))
# elif choice == "3":
#     print(num1,"*",num2,"=", multiply(num1,num2))
# elif choice == "4":
#     print(num1,"/",num2,"=", divide(num1,num2))
# else:
#     print("Invalid Input")


# def fact(x):
#     if x == 1:
#         return x
#     else:
#         return x * fact(x - 1)
# Num = int(input("Enter a number: "))
# if Num < 0:
#    print("Sorry, factorial does not exist for Negative numbers")
# elif Num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of",Num,"is",fact(Num))


# i = 1
# while i <=5:
#     print("Anshika")
#     i= i+1

# i = 1
# while i <=5:
#     print("Anshika ", end="")
#     j = 1
#     while j<=4:
#         print("Tiwari ", end="")
#         j=j+1
#     i= i+1
#     print()

