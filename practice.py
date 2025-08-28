# printing all reverse numbers from 10 to 1
from operator import truediv
from urllib import request
from xml.dom import WrongDocumentErr

# for i in range(10,0,-1):
#     print("the reverse numbers are",i)


# printing character of the word programming

# for i in "programming":
#     print("letters are", i)
# for i in range(2,22,2):
#     print(i)

# for i in range(1,6):
#     print('#'*i)

# for i in range(1,11):
#     print(i**2)

# vowels = ['a', 'e', 'i', 'o', 'u']
# string = 'Hello World'
#
# for i in string.lower():
#     if i in vowels:
#         print(i)


# while True:
#     num = int(input('enter number'))
#     if num < 0:
#         print("number is negative")
#         break
#     else:
#         print('numbers is', num)
# count = 1
# while count <= 100:
#     print(count)
#     count += 1

# count = 0
# i = 1
# while i<= 100:
#     count+=i
#     i+=1
#     print('count is:', count)


# for i in range(1,100,2):
#     print(i)


# i = 1
# while i<= 100:
#     count = i+2
#     print(count)
#     i+=2

# i = 10
# while i>= 1:
#     print(i)
#     i -=1
#
# print('liftoff!!!')


# num = int(input('enter a number:'))

# i = 1
#
# while i <=10:
#     result = num * i
#     print(num,'*',i,'=',result)
#     i=i+1

# for i in range(1,30):
#     result =  num * i
#     i= i+1
#  print('multuplication table of', num,'is', num,'*',i,'=',result)


# import math
# lst = [2,-2,55,66,89,-10]
# i = 0
# while i < len(lst):
#     if lst[i] > 0:
#         print(lst[i])
#     i+=1

# import math as m
#
# lst = [2, -2, 55, 66, 89, -10]
# i = 0
#
# while i < len(lst):
#     if lst[i] > 0:
#         print(lst[i])
#     i += 1

# for i in range(100, 0,-1):
#     print(i)
#
# i = 10
# for i in range(10,0,-1):
#     for j in range(1, i+1):
#         print(j,end='')
#     print()

# n = int(input())
# i = 0
# while i < n:
#     print(i ** 2)
#     i += 1

# n = int(input())
#
# for i in range(1, n+1):
#     print(i,end='')


# for i in range(1,10):
#     if i%2==0:
#         continue
#     print(i)
# print('its done!!')


# sym = '#####'
# i=1
# while i<=5:
#     print(sym)
#     i+=1

# for i in range(4):
#     for j in range(4):
#         print('#',end='')
#
#     print()

# for i in range(4):
#     for j in range(4-i):
#         print('#',end='')
#
#     print()

# num = 7
#
# for i in range(2,num):
#     if num % i == 0:
#         print("not found")
#         break
# else:
#     print('prime')


import array as arr

#
# vals = arr.array('u',['a','e','i','o','u'])
#
#
# for i in range(len(vals)):
#     print(vals[i])

# num =arr.array('i',[])
#
#
# n = int(input("enter lenght of array:"))
#
# for i in range(n):
#     x = int(input("enter element:"))
#     num.append(x)
#
# print(num)
#
# req =  int(input("enter request:"))
# print(num.index(req))
# k = 0
# for i in num:
#     if req == i:
#         print('element', req,'foud at index::', k)
#     else:
#         k+=1

# 1️⃣ Write a program to create an array of integers and display it.
# 2️⃣ Take n integers from the user and store them in an array.
# 3️⃣ Find the maximum and minimum elements in an array.
# 4️⃣ Count the number of even and odd numbers in an array.
# 5️⃣ Search for an element in an array and print its index (if it exists).
# 6️⃣ Reverse the elements of an array.
# 7️⃣ Print the sum of all elements of an array.
# 8️⃣ Print the product of all elements of an array.
# 9️⃣ Replace all even numbers in the array with 0.
# 🔟 Find the second largest element in the array.


import array as arr

# val = arr.array('i',[])
# size = int(input("Enter the size of the array: "))
#
# for i in range(size):
#     num = int(input("Enter the number: "))
#     val.append(num)
#
# print('array of integer:', val)
# print('maximum element in an array is:',max(val))
# print('minimumm element in an array is:',min(val))


# print(val.sort())

# val = arr.array('i',[1,2,3,4,5])
# print('second largest elemnt', val[-2])
#
# for i in range(len(val)):
#     if val[i] % 2 == 0:
#         print(val[i],'is even')
#     else:
#         print(val[i],'is odd')
# ind = int(input("Enter the index of the integer: "))
# print('the index value for the integer',ind,'is:',val.index(ind))
# val.reverse()
# print(val)
# sum = 0
# for i in val:
#     sum = sum + i
# print('sum is ::', sum)
# mul = 1
# for i in val:
#     mul *=i
# print('multiplication is:', mul)

# for idx in range(len(val)):
#     if val[idx] % 2 == 0:
#         val[idx] =0
# print('even bcms zeo',val)

# 1️⃣1️⃣ Sort an array in ascending and descending order.
# 1️⃣2️⃣ Remove all duplicate elements from an array.
# 1️⃣3️⃣ Count the frequency of each element in an array.
# 1️⃣4️⃣ Merge two arrays into one and sort the result.
# 1️⃣5️⃣ Split the array into two halves and print them.
# 1️⃣6️⃣ Rotate the array to the right by k steps.
# 1️⃣7️⃣ Find the sum of positive and negative numbers separately.
# 1️⃣8️⃣ Check if the array is a palindrome (reads the same forward & backward).
# 1️⃣9️⃣ Find the difference between the largest and smallest element.
# 2️⃣0️⃣ Replace every element with the sum of its neighbors.



import array as arr

 # i in range(len(num)):
#     for j in range(i+1,len(num)):
#      # num = arr.array('i',[1,3,2,40,5])
# #
# # sorted(num)
# #
# # num.reverse()
# # print(num)
#
# # num = arr.array('i',[1,3,3,2,40,5,3])
# # print('array', num)
# # print('duplicat')
#
# # for   if num[i] == num[j]:
#             print(num[i])
#             break

# i=0
# while i < len(num):
#     j = i + 1
#     while j < len(num):
#         if num[i] == num[j]:
#             print(num[i])
#         j += 1
#     i = i + 1
# num.count()

# import array as arr
#
# val = arr.array('i', [2, 3, 4, 55, 7, 2, 3, 1])
#
# print(val)
# print('duplicates:')
#
# count = 0
# printed = set()
#
# for i in range(len(val)):
#     for j in range(i + 1, len(val)):
#         if val[i] == val[j] and val[i] not in printed:
#             print(val[i])
#             count += 1
#             printed.add(val[i])
#             break
#
# print("Number of duplicate elements:", count)

# import array as arr
#
# num1 = arr.array('i', [1, 3, 7,1,0,9,8])
# num2 = arr.array('i', [4, 5, 6])
#
# for i in range(len(num2)):
#     val1 = num2[i]
#     print(val1)
#     num1.append(val1)
# print(num1)
# sorted = sorted(num1)
# sort_list = arr.array('i', sorted)
# print(sort_list)


# import qrcode

# data = 'Vaibhav Atiwadkar'

# qr = qrcode.make(data)

# qr.save("qrcode.png")
# print("QR code generated successfully!!")


