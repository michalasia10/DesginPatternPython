import random


class DataBase:
    _instance_ = None

    def __init__(self):
        id = random.randint(1,101)
        print(f'{id}')

    def __new__(cls, *args, **kwargs):
        if not cls._instance_:
            cls._instance_ = super(DataBase,cls).__new__(cls,*args,**kwargs)
        return cls._instance_


if __name__ == '__main__':
    d1= DataBase()
    d2 = DataBase()
    print(d1 == d2)