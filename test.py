a = 5
print(a)
a = 'str'
print(len(a))


class Person:
    def __init__(self, name):
        self.name = name

    def sayName(self):
        '''
      这是一个展示名字的方法
      '''
        print(self.name)

    def run(self):
        '''
      奔跑
      '''
        print('%s快乐的奔跑' % self.name)


b = Person('cheng')
c = Person('sun')
d = Person('guo')
b.sayName()
c.sayName()
d.sayName()
d.run()

f = '3'


class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('%s拿到了~~~~' % self._name)
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        print('设置%s成功了~~~~' % self._name)

    def run(self, distance):
        print('%s奔跑了%d米！！！' % (self._name, distance))

    def sleep(self):
        print('%s睡觉！！！' % self._name)


class Dog(Animal):
    pass


dog = Dog('狗')
dog.run(3)
r = isinstance(dog, object)
g = issubclass(Animal, object)
print(g)
