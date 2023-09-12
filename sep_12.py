# # # Collections in Python
# # """
# # Ordered     Immutable   string      "ahfahdxsd"
# # Ordered     Mutable     list        [1,2,3]
# # Ordered     Immutable   tuple       (1,2,3)
# # Unordered   Mutable     set         {1,2,3,5}
# # Unordered   Mutable     Dict         {"name":"prarthana"}
# #
# # Two special collections:
# # strings: Ordered & Immutable collections of characters              " "/ ' '
# # dictionaries: Unordered & Mutable collections of key-value pairs
# # """
# #
# # # # list: Ordered & Mutable collection of members
# # list1=[1,2,3,4,5,6,7,8,91,0]
# numbers = [33,12, 0, -125, 44, 33, 4791234, -5592, 33]
# # # index     0  1    2     3   4
# # #          -9 -8    -7
# # print(numbers)
# # input(numbers)
# # print(len(numbers))
# # print(type(numbers))
#
# numbers = [33,12, 0, -125, 44, 33, 4791234, -5592, 33]
# # s=("abc",123)
# # # # s=123456789
# # print(list(s))
# print(numbers[8:2:-2])
# #
#
#
# # print altrenate elements from list
# #
# # perform addition between first and last element
# #
# # get reverse of the list
# # num=[1,2,3,4,5]
# # print(num[::2])
# # print(num[0] + num[-1])
# # print(num[0] + num[len(num)-1])
# # print(num[::-1])
# # print(num[len(num)-1::-1])
# #
# # "abc"
# numbers = [33,12, 0, -125, 44, 33.4, 4791234.0, -5592, 333]
# # numbers=["aa","ab","b"]
# print(min(numbers))
# print(max(numbers))
# # vegetables = ["carrot", "tomato", "potato", "spinach", "cucumber", "beetroot", "Lnion", 8.5]
# # print(vegetables)
# # print(min(vegetables))
# # print(max(vegetables))
#
# #
# # numbers=[33, 0, -125, 44, 33, 4791234, 8863, 33]
# #
# #
# vegetables = ["carrot", "tomato", "potato", "spinach", "cucumber", "beetroot", "Lnion", "a"]
# # # print(min(numbers))
# # # print(max(numbers))
#
# print(sorted(vegetables))
# print(sorted(numbers, reverse=True))
#
# # mix_veg = [1.23, 1.1, 1]
# # # print(mix_veg)
# # print(min(mix_veg))
# # print(sorted(numbers,reverse=True))
# # # list1=list(s1)
# # print(list1)
#
# # print(numbers[2:5:1])
# """
# print(len(numbers))
# print(numbers)
# print(type(numbers))
# characters = list('Krushnam')
# print(characters)
#
# print(min(numbers))
# print(max(numbers))
# sorted_numbers = sorted(numbers)    # sorted() will always give you a NEW LIST
# print(numbers)
# print(sorted_numbers)
#
# print(sorted(numbers, reverse=True))
#
# vegetables = ["carrot", "tomato", "potato", "spinach", "cucumber", "beetroot", "onion", "Lemon"]
# print(vegetables)
# print(min(vegetables))
# print(max(vegetables))
#
# mix_veg = ["carrot", 3, "tomato", 1.5, "spinach", -0.5]
# print(mix_veg)
# # print(min(mix_veg))
# """
# # Ordered means
# """
# +ve & -ve Index numbers of each element
# Accessing through +ve or -ve index
# slicing is exactly the same as it was in strings
#
# print(numbers[3])
# print(mix_veg[3])
# print(numbers[2 : -2 : 2])
# """
# # numbers=[33, 10, -125, 44, 33, 4791234, -5592, 33]
#
# # numbers[0]=3333
# # print(numbers)
#
# # 1) len()
# # 2) type()
# # 3) list()
# # 4) min()
# # 5) max()
# # 6) sorted()
#
#
# # methods:for adding elememts
# # numbers=[33, 10, -125, 44, 33, 4791234, -5592, 33]
# # numbers2=["55"," "," "]
# # # 1)append()
# # print(numbers)
# # numbers.append("123")
# # # print(numbers)
# #
# # numbers.insert(0,"abc")
# # print(numbers)
# #
# # numbers.extend(numbers2)
# # numbers.append(["55"," "," "])
# # numbers.append(None)
# # print(numbers)
# # numbers.append("12345")
# # # numbers.append("12345")
# # # print(numbers)
# # # Mutable
# # # numbers[3] = 119.8
# # # print(numbers)
# #
# # # list methods
# # numbers.append(2000)
#
# # numbers.append(3000)
# # print(numbers)
# # numbers.append(3000)
# # numbers.append(3000)
# # print(numbers)
# # numbers.append(3000)
# # print(numbers)
# #
#
# # methods for deleting the elements
# numbers=['a',2,3]
# # print(numbers)
# # numbers.clear()
# # print(numbers)
# # numbers.append(1)
# # print(numbers)
# # del numbers
# # print(numbers)
# # numbers.remove(2)
# # print(numbers)
# # numbers.pop(2)
# # print(numbers)
# #
# # print(numbers.count(10))
# #
# # s1="sssss"
# # s2=['s','a']
# # print(s1.count('x'))
# # print(s2.count('aeiou'))
#
#
#
# li=[1,2,3,4,5,6,7,8,9,0]
# # output:
# # [1,3,5,7,9]
# # [1,0]
# # [1,2,3,4,5,6,7,8,9,0,"i",55]
# # [1,2," ",3,4,5,6,7]
# # count space from this [1,2," ",3,4,5,6,7," "]
# # delete list1 and show the eleemnt of list1
#
# # li=[1,2,3,4,5,6,7,8,9,0]
# # li.insert(11," ")
# # print(li)
# # print(li.count(1))
#
# l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]
# # l2=l1
# l2=l1.copy()
#
# l1.clear()
# # l2 = l1.copy()
# print(l2)
#
# # # del l1
# # # print("Before:")
# # # # print("l1 =", l1)
# # # print("l2 =", l2)
# # # l3 = l1
# # # print("l3 =", l3)
# #
# # # l1.append(5000)
# #
# # # print("After:")
# # # print("l1 =", l1)
# # # print("l2 =", l2)
# # # print("l3 =", l3)
# #
# # # del l1
# # # print(l1)
# # l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]
# # l2=[100,500,"abc"]
# # l1.extend(l2)
# # print(l1)
# # l1.insert(4, "5")
# # print(l1)
# # # l2 = [100, 200, [300,123]]
# # # l3=[1]
# # # l1.append(l2)
# # #
# # # l2.extend(l3)# print(len(l1))
# # # l1.extend(l2)
# # # print(l1)
# #
# # # l3 = "Python"
# # # l1.extend(l3)
# # # print(len(l1))
# # # print(l1)
# #
# l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]
# print(l1.index(44.6))
# print(l1)
#
# # # # print(l1.index(33, 4))
# # print(l1.index(33, 4, 6))
# #
# # #
# # # print(l1)
# # li=["123",1,2,3]
# # # print(l1.pop())
# # print(li.pop(0))
# # # # print(l1.pop(500))
# # print(li)
# #
# # li.remove(1)
# # # # print(l1.remove(-50592.44))
# # # print(li)
# l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]
# l1.append(['1'])
# l1.extend(['1'])
l1=[1,2,3,4]
print(l1)
l1.reverse()
print(l1)#----> new list
l2=list(reversed(l1))#----->object
print(l1)
#
#
# # print("l1 =", l1)
# # print(list(reversed(l1)))
# #
# sorted(l1,reverse=True)
# l1.sort()
# l1.sort(reverse=True)
# print("l1 =", l1)

# l1.reverse()
# print("l1 =", l1)

# list1=[100,45,23,67,123,67,89]
#
# output:
# 1) minimun
# 2)maximum
# 3)asecding
# 4)desending

# list1=[1,2,3,4]
# 5)list2=["!","123",""] add this list to list1
# 6) delete list1 and print list1
#
#
# delete list
# print(list2)

# list2=[1,2,3]
# print(sum(list2))
#
# list1[2,56,34,67,89]
#
# total of list1
# use reversed on list1
# [2,34,89]



# Next Class: Operators in Python, decision making, loops, remaining collections

