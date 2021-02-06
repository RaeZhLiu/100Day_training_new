class Person(object):
    """定义Person类"""
    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


if __name__ == '__main__':
    person = Person("王大锤", 12, 180)
    person.play()

    person.age = 22
    person.name = "小王"

    person.play()

    person._weight = 200
