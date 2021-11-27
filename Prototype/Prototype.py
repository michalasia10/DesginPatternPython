import copy


class Address:
    def __init__(self,street_addres,city,country):
        self.street_adress = street_addres
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_adress}, {self.city}, {self.country}'




class Person:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


john = Person('John',Address('123 London Road','London','UK'))
jane = copy.deepcopy(john)
jane.address.street_adress = '124B London Road'
print(john,
      '\n',
      jane)