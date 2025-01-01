salaries = ['$400', '$5000', '$6000']
salaries2 = [int(i[1:]) for i in salaries]
print(salaries2)

names = ['Fatoom', 'Mohammed', '', 'Fayad']
names2=[name for name in names if name!='']
print(names2)

x = [1, 5, 8]
y = [i**2 for i in x]
print(y)

dates = ['01-01-2020', '05-05-2022', '06-08-2023','04-10-2019']
years = [int(d[-4:]) for d in dates]
print(years)

names_alt = ['Fatoom', 'Mohammed', '', 'Fayad']
names3=[name if name!='' else 'Unknown' for name in names ]
print(names3)
