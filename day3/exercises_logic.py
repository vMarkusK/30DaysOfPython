a = 'python'
b = 'dragon'

print(len(a))
print(len(b))

print(len(a) != len(b)) 

print('on is in python', 'on' in a) 
print('on is in dragon', 'on' in b) 

print('on is not in python', 'on' not in a) 
print('on is not in dragon', 'on' not in b) 

print(str((float(len(a)))))

print(type('10') == type(10))

print(int(9.8) == 10)

number = 1
count = 0
multiply = [1, 2, 3, 4, 5]
for x in multiply:
    count += 1
    print(count, number, number * x, number * x * x, number * x * x * x)

