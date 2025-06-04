class Employee:
    Name="Edwin"
    company="DGBT"
    def get_salary(self):
        print(f"NAME is {self.Name} and company is {self.company}")
        print("Salary not decided")

    @staticmethod
    def ifemp():
        print("yes he is an employee")

Kumar=Employee()
Kumar.age=21
Kumar.get_salary()
Kumar.ifemp()