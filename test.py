class person:

    def __init__(self, name, surname,email, year_of_birth):
        self.abc = name
        self.surname = surname
        self.email = email
        self.year_of_birth = year_of_birth

    def age(self, currant_year):
        return currant_year - self.year_of_birth

anuj_var = person('anuj', 'yadav','anuj@gmail.com',1991)
ra = person ('rahul', 'yadav', 'rahul@gmail.com', 1992)
sa = person ('sahil', 'rao', 'sahil@gmail.com', 1995)

print(ra.abc + ' '+  ra.surname)
print(ra.age(2022))


class pop :

    def age (self, currant_year, date_of_birth):
        return currant_year - date_of_birth

    def email_id (self, email_id) :
        print('print the email_id take from user', email_id)

    def ask_name(self):
        name = input('tell me your name')
        return name

    def ask_dob(self):
        dob = input('enter your dob')
        return dob

anuj = pop()
rahul = pop()
nimmi = pop()

nimmi.email_id('nimmi@gmail.com')