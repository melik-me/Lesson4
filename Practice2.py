# Функция, которая выводит второе по возрастанию значение из
# переданных аргументов.

def premin(*args):
    l = list(args)
    a = min(l)
    n = l.count(a)
    for i in range(n):
        l.remove(a)
    a = min(l)
    return a

x = premin(9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, 0, -1, 2, 3, 4, 5, -2)
print(x)