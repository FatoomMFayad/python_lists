x = [1, 5, 5, 8, 7, 9, 44]

for i in x:
    print(i**2)


#slaries tax
salaries = [5000, 1500, 2500, 4000]
net_salaries = []
for salary in salaries:
    net_salaries.append(salary - 0.05*salary)
print(net_salaries)