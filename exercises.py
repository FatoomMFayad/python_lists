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

#7.	Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del(sample[0])
del(sample[-2])
del(sample[-1])
print(sample)
#8.	Write a Python program to print the numbers of a specified list after removing even numbers from it
lst = [1, 5, 4, 6, 8, 9, 11]
odd_numbers = [num for num in lst if num % 2 != 0]
print(odd_numbers)

#9.	Write a Python program to convert a list of characters into a string
chars = ['h', 'e', 'l', 'l', 'o']
my_string = ''
for char in chars:
    my_string+=char
print(my_string)

#10.	Write a Python program to get unique values from a list
names = ['Sally', 'Dalia', 'Sally', 'Hend', 'Nour', 'Ola', 'Hend']
unique = []
[unique.append(n) for n in names if n not in unique]
print(unique)

#11.	Write a Python program to count the number of elements in a list within a specified range
# Define the list of numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Define the range
lower_bound = 30
upper_bound = 70

# Use range to define the specified range
specified_range = range(lower_bound, upper_bound + 1)

# Count the number of elements in the range
specified = [num for num in numbers if num in specified_range]
count = len(specified)

# Print the result
print(f"Number of elements in the range [{lower_bound}, {upper_bound}]: {count}")