x = [1, 5, 3, 5, 9, 8, 5]
# count number of occurrences of 5 in x
print(x.count(5))
# reverse the list using reverse function
x.reverse()
print(x)

# reverse the list using reversed function'
y = list(reversed(x))
print(y)

#append two lists
first_list = [1, 5, 3, 5, 9, 8, 5]
second_list = [100, 200, 300, 500]
first_list.extend(second_list)
print(first_list)