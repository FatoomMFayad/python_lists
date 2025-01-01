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

#dealing with dates in list
dates = ['01-01-2020', '05-05-2022', '06-08-2023','04-10-2019']
years = []
for d in dates:
    years.append(int(d[-4:]))
print(years)

#greater than or equal 100
sales = [100, 150, 90, 30, 110, 210, 35]
for s in sales:
    if s >= 100:
        print(s)
#count odd and even numbers in list
numbers = [7, 2, 12, 4, 7, 23, 5,21, 22, 60, 41, 46]
even_cnt = 0
odd_cnt = 0
for number in numbers:
    if number % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
print(f"count of even numbers = {even_cnt}, and count of odd numbers = {odd_cnt}")

five_multipliers = []
for number in numbers:
    if number % 5 == 0:
        five_multipliers.append(number)
print(five_multipliers)