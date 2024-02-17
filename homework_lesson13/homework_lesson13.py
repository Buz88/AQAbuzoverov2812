#Створіть класс з описом будь-якої тварини. Додайте 1 static method

class animal():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def make_noize(self):
        pass

    @staticmethod
    def sleep():
        print("Animal is sleeping")

cat = animal(name="cat", age=12,weight=100)
cat.sleep()
print(f'name:{cat.name}, age:{cat.age}, weight: {cat.weight}.')
#Створіть класс з описом будь-якої компанії чи організації. Додайте 1 classmethod

class Company:
    total_employees = 0

    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        self.employees = []
    def hire_employee(self, employee_name):
        self.employees.append(employee_name)
        Company.total_employees += 1
    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

company = Company(name="ABC Corp", industry="Technology")
company.hire_employee("jane")
company.hire_employee("alex")
company.hire_employee("suzan")

print(f"Total employees in {company.name}: {Company.get_total_employees()}")