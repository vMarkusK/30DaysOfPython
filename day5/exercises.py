lst = list()
fruits = ['banana', 'orange', 'mango', 'lemon', 'apple', 'grape']
print(len(fruits))
first_fruit = fruits[0]
last_fruit = fruits[-1]
middle = len(fruits) / 2
print(middle)
middle_fruit = fruits[int(middle)]
print(first_fruit)      # banana
print(last_fruit)       # grape
print(middle_fruit)      # lemon
mixed_data_types = ['Markus', 18, 193, 'married', 'Antares 3']
it_comp = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'VMware']
print(it_comp)
print(len(it_comp))
first_comp = it_comp[0]
last_comp = it_comp[-1]
middle = len(it_comp) / 2
print(middle)
middle_comp = it_comp[int(middle)]
print(first_comp) 
print(last_comp)
print(middle_comp)
it_comp[0] = 'Veeam'
print(it_comp)
it_comp.append('Citrix')
print(it_comp)
it_comp.sort()
print(it_comp)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)
print(ages)
ages.sort()
average = sum(ages) / len(ages)
print(average)


