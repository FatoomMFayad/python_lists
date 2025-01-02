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
