class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name}, {self.position}, {self.date_of_birth}'

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self,name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def work_as(self,job):
        self.person.position = job
        return self

class PersonBirthBuilder(PersonJobBuilder):
    def born(self,date):
        self.person.date_of_birth = date
        return self

pb = PersonBirthBuilder()
me = pb.called('Michal').work_as('Programmer').born('1998').build()
print(me)