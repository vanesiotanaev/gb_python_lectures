# # Данные, функции и модули в Python

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # данные не перезаписываются
# data.writelines(colors)
# data.close() # закрываем процесс взаимодействия с файлом, чтобы избежать утечек в памяти

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w') # данные перезаписываются
# data.writelines(colors)
# data.write('\nLINE 2\n') # \n -- разделитель
# data.write('LINE 3\n')
# data.close()

# Другой способ через with

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import lection1 

# print(lection1.f(1)) # где lection1 - файл нашего предыдущего семинара,
# #  f - название одной из функций в нем

# import lection1 as l

# print(l.f(1))
# # то же самое

# если хотим много аргументов засунуть в функцию
# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', '1', 'd'))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортежи

# a = (3, 4)
# print(a)
# print(a[-2])

# Кортеж - список, который нельзя изменить

# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)

# Множества
# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a.add('red')
# print(a)

# a.remove('red')
# print(a)

# a.discard('red')
# print(a)

# a.clear()
# print(a)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}
# print(q)

# Неизменяемое множество

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

list1 = [1,2,3,4,5]
list2 = list1

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print()

list1[0] = 123

for e in list1:
    print(e)
print()

for e in list2:
    print(e)

print(list1.pop())
print(list1)

print(list1.insert(2,11))
print(list1)

print(list1.append(444))
print(list1)
