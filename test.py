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