class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print('Role is:',self.role)
        print('Department is:',self.department)
        print('Salary is:',self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__('assocuntant','finance',70000)

    def showDeatail(self):
        print('Name is:',self.name)
        print('Age is:',self.age)
        super().showDetails()

eng=Engineer('vaibhav',23)
eng.showDeatail()


