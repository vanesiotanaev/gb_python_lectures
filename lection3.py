# # Анонимные методы или lambda-функции нужны, чтобы не прописывать отдельно
# # метод, который в программе будет использован один-два раза.

# def f(x):
#     x**2

# g = f #Функцию можно положить в переменную. Как видно из принтов,
#         # работает все одинаково. Значит, можно в функцию преедать в качестве аргумента функцию.

# print(f(1))
# print(g(1))


# def f(x):
#     return x**2

# print(f(2))

# #Чтобы использовать лямбда-функции, нужно посмотреть тип данных той функции,
# # для которой мы написали бы метод. 
# print(type(f))

# g = f
# print(type(g))

# print(f(4))
# print(g(4))
# def calc(x):
#     return x+10

# def calc2(x):
#     return x*10

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc, 10)

#####################
# def mult(x, y):
#     return x * y

def math(op, x, y):
    return op(x, y)

g = math

# print(g(mult, 2, 2))
##################### OR #################

# mult = lambda x, y: x*y

# print(g(mult, 2, 2))
############# OR ##########################

# print(g(lambda x, y: x*y, 4, 5))

# LIST COMPREHENSION

# 1.
# list = [i for i in range(1, 21) if i%2 == 0]
# print(list)
# # 2.
# def f(x):
#     return x**3
# list = [f(i) for i in range(1, 21) if i % 2 == 0]
# print(list)
# 3. 
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# 4. 
li = [x for x in range(1, 20)]
print(li)

li = list(map(lambda x:x+10, li))
print(li)

# см. PDF