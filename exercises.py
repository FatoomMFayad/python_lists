#1.	Write a Python program to sum all the items in a list
from itertools import count

x = [1, 5, 8, 9, 10]
sum = 0
for i in x:
    sum+=i
print(sum)

#2.	Write a Python program to multiply all the items in a list.
multiply = 1
for i in x:
    multiply*=i
print(multiply)
#3.	Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
strings = ['abc', 'xyz', 'aba', '1221']
count = 0
for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1
print(count)

#4.	Write a Python program to clone or copy a list.
nums = [1, 2, 3, 4, 5]
y = [n for n in nums]
print(y)

#5.	Write a Python program to find the index of an item in a specified list
my_list = ['hi', 'hello', 'salam', 'bye']
indx = my_list.index('hello')
print(indx)

#6.	Write a Python function that takes two lists and returns True if they have at least one common member
first = ['hi', 'hello', 'salam', 'bye']
second = ['hello', 'salam', 'bye']
result = False
for i in first:
    if i in second:
        result = True
print(result)
