# Singleton using __init__ constructor method:
class One:
    __object = None

    @staticmethod
    def getObject():
        if not One.__object:
            One()
        return One.__object

    def __init__(self):
        if not One.__object:
            One.__object = self
        else:
            raise Exception("Cannot create multiple objects in Singleton class!")


obj1 = One()
print('First Object', obj1)

obj2 = One.getObject()
print('Second Object', obj2)

try:
    obj3 = One()
    print(obj3)
except Exception as e:
    print(e)


# Singleton using __new__ method:
class Two(object):
    __object = None

    def __new__(cls, *args, **kwargs):
        if not Two.__object:
            Two.__object = object.__new__(cls, *args, **kwargs)
        return Two.__object


obj1 = Two()
print('First Object', obj1)

obj2 = Two()
print('Second Object', obj2)