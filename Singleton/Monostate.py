class CEO:
    __shared_state = {
        'name':'Steve',
        'age':55
    }
    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate,cls).__new__(cls,*args,**kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.mone_managed = 0

    def __str__(self):
        return f'{self.name} manages {self.mone_managed}'

if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.name = 'Michal'
    ceo2.age = 77
    print(ceo1,'\n',ceo2)
    print('------------------------------------')

    cfo1 = CFO()
    cfo1.name = 'Sheyrl'
    cfo1.mone_managed = 1
    print(cfo1)
    cfo2 = CFO()
    cfo2.name = 'Deryl'
    cfo2.mone_managed = 2
    print(cfo1)
    print(cfo2)