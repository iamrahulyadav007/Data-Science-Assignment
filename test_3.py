class car :

        def __init__(self, body, enjine, tyre):
            self.body = body
            self.enjine = enjine
            self.tyre = tyre

        def milage(self):
            print('milage of the car is : ')

class tata(car):
    pass

t = tata('iron', 1250,17)
#print(t.milage())


class bank :

    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print('this will show you your account open status')
    def deposite(self):
        print('yhis will show you your deposite amount')

class hdfc_bank(bank) :
    def hdfc_to_icici(self):
        print('this will show you all the transaction happen to icici throght icici')

class icici(hdfc_bank):
    pass

i = icici()
#i.hdfc_to_icici()





class bank :

    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print('this will show you your account open status')
    def deposite(self):
        print('yhis will show you your deposite amount')
    def test(self):
        print('this is test method from bank')

class hdfc_bank :
    def hdfc_to_icici(self):
        print('this will show you all the transaction happen to icici throght icici')
    def test(self):
        print('this is test method from hdfc_bank')

class mere_bank :
    def mere_account_status(self):
        print('this will show you all the transaction happen to mere bank')

class icici (hdfc_bank, bank, mere_bank) :
    pass

i = icici()
#i.mere_account_status()



class ineuron :
    def student(self):
        print('all the student')
    def achivers(self):
        print('all the achivers')
    def hall_of_fame(self):
        print('all the hall_of_fame')

class i_vision(ineuron):
    def student(self):
        print('these are the filter student list')

iv = i_vision()
#iv.student()



class meri_class :
    __student = 'data science student'

    def student_class(self):
        print('print the class of student',meri_class.__student)

i = meri_class()
#i.student_class()
#print(i._meri_class__student)

list()



class ineuron:
    __students = "data science"

    def studetns(self):
        print(ineuron.__students)

i = ineuron()
#i.studetns()
#print(i.)

list()



class ineuron:
    def __init__(self):
        self.students1 = "data science "

    def students(self):
        print(self.students1)

i = ineuron()
#i.students()
#i.students1 = "data analytics"
#i.students()

class ineuron1:
    def __init__(self):
        self.__students1 = "data science "

    def students(self):
        print(self.__students1)
    def student_change(self,new_value):
        self.__students1 = new_value

i1 = ineuron1()
#i1.students()
#i1.__students1 = "big data"
#i1.students()
#i1.student_change("sudhanshu")
#i1.students()






class meri :
    def student(self):
        print ('the students details')

class class_type :
    def student(self):
        print('the class type of students')

def i_ext(a) :
    a.student()

i = meri()
j = class_type()

i_ext(i)
i_ext(j)

pip install pymongo

import pymongo


client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)



