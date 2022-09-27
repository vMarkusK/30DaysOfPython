space = ' '
a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python' 
num1 = a + space + b + space + c + space + d
print(num1)

a = 'Coding'
b = 'For'
c = 'All'
num2 = a + space + b + space + c
print(num2)

company = num2
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[-7:])
print(company.index('Coding'))
print(company.replace('Coding', 'Python'))
print(company)

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True