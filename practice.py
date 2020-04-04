status_list = ['a', 'b', 'c', 'd', 'e']
print(status_list)
print(status_list[::-2])
my_list = ['f', 'g', 'h']
# print(status_list + my_list)
# print(my_list * 3)
print('f' in status_list)
a = max(status_list)
# del status_list[2]

print(status_list)
for s in status_list:
    print(s)
# 元组 tuple
my_tuple = 3, 4, 5, 10
x, *y, z = my_tuple
print('x =', x)
print('y =', y)
print('z =', z)
b = [1, 2, 3, 5, 6]
c = b
b[1] = 20
print('b =', b)
print('c =', c)
# 字典 (dictionary)
d = {'name': 'cheng', 'age': 31, 'weight': 55}
print(d['name'])
e = dict(name='sun', age=31, weight=48)
print('e =', e)


class Person():
    name = 'sun'

    def getName(self):
        print(self.name)


f = Person()
f.getName()