from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,20000)
        feaddr=faker.city()
        ffirst_name=faker.first_name()
        flast_name=faker.last_name()
        fdate=faker.date()
        femail=faker.email()
        #emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
        print(feno ,fename ,fesal ,feaddr ,ffirst_name  ,flast_name ,fdate,femail)
populate(10)
