# # The return Statement
# # The statement return [expression] exits a function,
# # optionally passing back an expression to the caller.
# # A return statement with no arguments is the same as return None.
#
# # Function definition is here
#
# # def my_function(**kid):
# #   print(kid["fname"] + kid["lname"])
# #
# # my_function(fname = int(input("enter one number")), lname = int(input("enter one number")))
#
#
# total=40
#
# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    total = arg1 + arg2
#    sub(arg2)
#    print("Inside the function : ", total)
#    return total
# def sub(arg1):
#     print(arg1-10)
# # #
# # # # Now you can call sum function
# sum( 10, 20 )
# # sub(total)
# print("Outside the function : ", total)
#
# # output:
# # prarthana kamleshbhai maheta
#

Sample_String='The quick Brow Fox'
# print(Sample_String.replace(" ",""))

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).

# # def print_name(m,f,l):
# #     return f"my full name is: {f} {m} {l}"
# # a=print_name(f="A",m="B",l="C")
# # print(a)
#
# # Default arguments
#
# # # Function definition is here
# # def printinfo( name, age=10 ):
# #    "This prints a passed info into this function"
# #    print("Name: ", name)
# #    print("Age ", age)
# #    return
#
# # # Now you can call printinfo function
# # printinfo( name="miki" )
# # print(a)
# # printinfo( name="miki" )
#
# #
# # Variable-length arguments
# # You may need to process a function for more arguments than you specified
# # while defining the function. These arguments are called variable-length arguments
# # and are not named in the function definition, unlike required and default arguments.
#
# # Function definition is here
# # a=1
# # a=2
# # a={"a":2}
# # print(a)
# # def printinfo( *args1,**arg1 ):
# #    "This prints a variable passed arguments"
# #    # (60,50)
# #    print(args1)
# #
# #    def print_name(arg1):
# #       print("Output is:",arg1)
# #       return
# #    print_name(arg1)
# #
# # # Now you can call printinfo function
# # printinfo( 10,20,40,80 )
# # printinfo( 70, 60, 50 )
#
#
#
# # Lambda function
# # A lambda function is a small anonymous function.
# #
# # A lambda function can take any number of arguments, but can only have one expression.
#
# # Why Use Lambda Functions?
# # The power of lambda is better shown when you use them as an anonymous function inside another function.
#
# # lambda arguments : expression
def sum(a):
    return a+10
print(sum(5))
#
x = lambda a,b=10 : a + b
# #
print(x(5))
#
x = lambda a, b : a * b
print(x(5, 6))
# # pets = ['cats', 'dogs', 'fishes', 'rabbits', 'hamsters', 'parrots', 'ferrets']
# # l1=[]
# # for word in pets[::-1]:
# #     l1.append(word)
# #     # print(word)
# # l1.sort()
# # print(l1)
# #
# # # pets=['a','c','d','b']
# # pets = ['cats', 'dogs', 'fishes', 'rabbits', 'hamsters', 'parrots', 'ferrets']
# # pets.sort(key=lambda word: word[::-1])
# # print(pets)
#
#
#
#
# product = lambda a: a**2
# print("The product is:", product(10))
# #
# text = (lambda x="Java", y = " is", z = " my favourite": x + y + z)
# print(text("Python","is not"))
#
#
#
# #
# # Scope of Variables
# # All variables in a program may not be accessible at all locations in that program.
# # This depends on where you have declared a variable.
# #
# # The scope of a variable determines the portion of the program where you can access a particular identifier.
# # There are two basic scopes of variables in Python −
# #
# # Global variables
# # Local variables
#
#
# # total = 0; # This is global variable.
# # # Function definition is here
# # def sum( arg1, arg2 ):
# #    # Add both the parameters and return them."
# #    total = arg1 + arg2; # Here total is local variable.
# #    print "Inside the function local total : ", total
# #    return total;
# #
# # # Now you can call sum function
# # sum( 10, 20 );
# # print "Outside the function global total : ", total
#
# def func_1(x):
#     # return func_2(x)
#     x1=lambda x : x*x if x==1 else x*1
#     return x1(x)
#
# def func_2(x):
#     if x ==1:
#         return x*x
#     else:
#        return  x*1
#
#
# print(func_1(2))
# print(x)
# lambda x : x*x if x==1 else x*1
# print(key(2))
# #
# # # 1

# Write a Python program to find whether a given year is a leap year or not.
#
# Test Data : 2016
#
# Expected Output :
# 2016 is a leap year
#
# # 2
# # Write a Python program to find the largest of three numbers.
# # Test Data : 12 25 52
# large=max(list1)
# small=min(list2)

# # Expected Execution:
# # 1st Number = 12
# # 2nd Number = 25
# # 3rd Number = 52
#
# #3
# # Take values of length and breadth of a rectangle from user and check if it is square or not.
#
# #4
# # Take values of length  of a square from user and find area of a square.


# 7. Write a Python program to find if a given string starts with a given character using Lambda.
# Sample Output:
# True
# False
#
# 13. Write a Python program to count the even and odd numbers  of integers using Lambda.
# Original arrays:
#
#  3 = odd
#  4 = even

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #######################1#######################
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
# year = int(input("Enter a year: "))
#
# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
#
#
#
# ##############################2########################
# # def find_largest_number(a, b, c):
# #     if a >= b and a >= c:
# #         return a
# #     elif b >= a and b >= c:
# #         return b
# #     else:
# #         return c
# #
# # # Input three numbers
# # num1 = float(input("Enter the 1st number: "))
# # num2 = float(input("Enter the 2nd number: "))
# # num3 = float(input("Enter the 3rd number: "))
# #
# # largest_number = find_largest_number(num1, num2, num3)
# #
# # print("1st Number =", num1)
# # print("2nd Number =", num2)
# # print("3rd Number =", num3)
# # print(f"The largest number is {largest_number}")
#
#
# ################3##########################
#
# length = float(input("Enter the length of the rectangle: "))
# breadth = float(input("Enter the breadth of the rectangle: "))
#
# if length == breadth:
#     print("It is a square.")
# else:
#     print("It is not a square.")
#
#
# #########################4####################
# def calculate_square_area(side_length):
#     area = side_length ** 2
#     return area
#
# # Input the length of the square's side from the user
# side_length = float(input("Enter the length of the square's side: "))
#
# # Calculate the area of the square
# area = calculate_square_area(side_length)
#
# print(f"The area of the square with side length {side_length} is {area}")


# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
# num3 = float(input("Enter the 3rd number: "))
#
# l1=lambda num1,num2,num3: print("a is first",num1) if num1>=num2 and num1>=num3 else None

# if num1<num2 or num3<num2:
#     print("b is second",num2)
# elif num1<num3

# l3=lambda num2,num3:print("c is second",num3) if num3<=num2 else print("b is second",num2)
# max1=l1(num1,num2,num3)
# max3=l3(num2,num3)
# print(max1)
# l2=lambda

# def m2m(a,b,c):
#     if a>=b and a>=c:
#         print("a is first")
#
# m2m(4,5,6)

# l1=[num1,num2,num3]
# max1