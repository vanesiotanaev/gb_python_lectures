print('hello')
a = 1.23
print(a)
value = None
value = 1234
print (value)
print(type(value))

str = 'hello world'
print(str) #print string
print(a, '*', value, str)
print(f'{a} - {value} - {str}')
print('{1} - {2} - {0}'.format(a, value, str))


f = True
print(f)

list = []
print(list)

list1 = [1, 2, 3, '*']
print(list1)

#Вывод и ввод данных
print('Type a: ')
a = int(input())
print(a)

#Арифметические операции
a = 12
b = 8
c = a+b
print(c)

c = a / b
print(c)

c = a // b #Целые числа
print(c)

#raise to the power 
m = 2
n = 3
g = m ** n
print (f'{m} to the power of {n} equals {g}')

#Нет ограничения по хранению данных
m = 2
n = 800
g = m ** n
print (f'{m} to the power of {n} equals {g}')

m = 1.31232
n = 3
g = round(m * n, 5)
print (g)

#Сокращенные операции
a = 3
a += 5
print(a)

#Логические операции
a = 1 > 3
print(a)
a = 1 < 3
print(a)

a = 1 > 3 and 5 > 2
print(a)

a = 1 > 3
print(a)

#Большие неравенства
a = 1 < 3 < 5
print(a)

#Логические операции 
f = 1 > 2 or 4 < 6
print(f)

f = [1, 2, 3, 4]
print(f)
print(2 in f)

f = [1, 2, 3, 4]
print(f)
is_odd = f[0] % 2 == 0
print(is_odd)