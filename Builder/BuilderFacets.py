class Person:
    def __init__(self):
        self.street_adress = None
        self.post_code = None
        self.city = None
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Address {self.street_adress}, {self.post_code},{self.city}' + \
               f'Employee at {self.company_name} as a {self.post_code} earing {self.annual_income}'


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earing(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_adress):
        self.person.street_adress = street_adress
        return self

    def with_postcode(self, postcode):
        self.person.post_code = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self

pb = PersonBuilder()
person = pb.lives.at('123 London Road').in_city('London').with_postcode('SW12BC').works.at('Fabrikan').as_a('Engineer').earing(123000).build()
print(person)