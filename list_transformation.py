salaries = ['$400', '$5000', '$6000']
salaries2 = [int(i[1:]) for i in salaries]
print(salaries2)

names = ['Fatoom', 'Mohammed', '', 'Fayad']
names2=[name for name in names if name!='']
print(names2)