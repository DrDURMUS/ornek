class Employee:
    arise_amount=1.04
    num_of_emp=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        #self.email=first + '.' +last + '@company.com'
        Employee.num_of_emp+=1
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print('deleted name!')
        self.first=None
        self.last=None
    def apply_raise(self):
        self.pay=int(self.pay*self.arise_amount)
        #self.pay = int(self.pay * Employee.arise_amount)
        #self.pay=int(self.pay*1.04)

    def __repr__(self):
        return "Employee('{}' '{}' {})".format(self.first, self.last, self.pay)
    def __str__(self):
        return '{}-{}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    @classmethod
    def set_arise_amount(cls,amt):
        cls.arise_amount=amt
    @classmethod
    def from_str(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() in [5,6]:
            return False
        return True

class Developer(Employee):
    arise_amount = 1.5
    def __init__(self,first,last,pay,prog_lan):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        self.prog_lan=prog_lan
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees==None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rmv_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.fullname())

emp_1=Employee('durmus','durmaz',3000)
emp_2=Employee('Seyma','Guner',5000)
#print(emp_1.email)
#print(emp_2.fullname())

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)
#print(emp_1.__dict__)
#print(Employee.__dict__)
#emp_1.arise_amount=1.5
#print(emp_1.__dict__)
#print(Employee.num_of_emp)

'''Employee.set_arise_amount(1.7)
emp_1.set_arise_amount(1.8)
print(Employee.arise_amount)
print(emp_1.arise_amount)'''

emp_str_1='John-Dove-4000'
emp_str_2='David-Kahn-4444'
emp_str_3='Tricha-Rackel-3000'

'''first,last,pay=emp_str_1.split('-')
new_emp_1=Employee(first,last,pay)
print(new_emp_1.email)'''
#new_emp_2=Employee.from_str(emp_str_2)
#print(new_emp_2.email)

'''import datetime
gun=datetime.date(2021,12,20)
print(Employee.is_workday(gun))'''


dev_1=Developer('durmus','durmaz',3000,'python')
dev_2=Developer('Seyma','Guner',5000,'java')
#print(dev_1.prog_lan)


mng_1=Manager('susan','parker',2333,[dev_2])
'''print(mng_1.email)
mng_1.print_emp()
print('\n')
mng_1.add_emp(dev_1)
mng_1.print_emp()
print(isinstance(mng_1,Manager))
print(issubclass(Developer,Employee))'''

#print(emp_1)
#print(emp_2+emp_1)
#print(len(emp_1))
print(emp_1.email)
print(emp_1.fullname)
emp_1.fullname='Durmus Durmaz'
print(emp_1.fullname)
del emp_1.fullname
print(emp_1)