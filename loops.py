x = [1, 5, 5, 8, 7, 9, 44]

for i in x:
    print(i**2)


#slaries tax
salaries = [5000, 1500, 2500, 4000]
net_salaries = []
for salary in salaries:
    net_salaries.append(salary - 0.05*salary)
print(net_salaries)

#dollars to dinars
dollars = [1000, 2000, 3000, 4000]
dinars = []
for dollar in dollars:
    dinars.append(dollar * 0.7)
print(dinars)

#revenues
revenues = ['$4000', '$3500', '$400']
sum = 0
for revenue in revenues:
    revenue = revenue.replace('$', '')
    sum+=int(revenue)
print(sum)

#another solution
total = 0
for revenue in revenues:
    total+=int(revenue[1:])
print(f"sum = {total}")