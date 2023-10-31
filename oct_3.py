#while
# i = 1
# while i <= 6:
#   print(i)
#   i += 1

#
# li=[1,6,3,5,6]
# for i in range(1,7):
#      print(i)

#while with break
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

#while with continue
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     continue
#   i += 1

# i = 1
# while i < 6:
#     for j in "abc":
#         print(j)
#         if j =='c':
#             print(i)
#         break
#     i+=1

# outerloop:for i in "abc":

# i = 0
# while i < 6:
#     pass

# for i in "abc":
#     for j in "def":
#         pass
#     # print(i)
#
# print(i)



# A function is a block of code which only runs when it is called.
#
# You can pass data, known as parameters, into a function.
#
# A function can return data as a result.

# def a_c_def():
#   print("Hello from a function")
#
# a_c_def()

# def my_function(a=1):
#     print(a + " Refsnes")
#
# # print(my_function())
# my_function("123","345")
# my_function("356")
# print(a)
#
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# A parameter is the variable listed inside the parentheses in the function definition.
#
# An argument is the value that is sent to the function when it is called

# def my_function(fname, lname):
#   print(fname + " " + lname)
#
# my_function("Emil", "Refsnes")


# ********Arbitrary Arguments, *args
# arguments that will be passed into your function, add a * before the parameter name in the function definition.
# def my_function(*kids,te,t):
#     print(kids)
#     for i in kids:
#         print("The youngest child is " + i[0])
# #
# my_function("Emil", "Tobias", "Linus","gchdgc","jhdwgdcye",tea="chai",t=1)
# ()


# Keyword Arguments
# You can also send arguments with the key = value syntax.
# def my_function( child2, child1,child3):
#   print("The youngest child is " ,child3)
#
# my_function(child1="Emil", child2="Tobias", child3="Linus")



# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments
# that will be passed into your function, add two asterisk:
# ** before the parameter name in the function definition.


# {
#     "fname":"1",
#     "lname":"2"
# }
# def my_function(**kid):
#   print(kid["fname"] + kid["lname"])
#
# my_function(fname = int(input("enter one number")), lname = int(input("enter one number")))



# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)

#
# create a function that calcualte the sum of list
# create a function that takes input from user as firstname and lastname, print them using keyword arguments
# create a function that find square of (2,3,5) using *args