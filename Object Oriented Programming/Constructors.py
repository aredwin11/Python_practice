class business:
    def __init__(self): #constructor --> no need to initialize the object
        print("Nice Company")
    def demo(self):
        print("good")

dell=business() #creating an object for it
dell.demo()

#default Constructor --> Takes only the self parameter and initializes with default values.
class Demo:
    def __init__(self):
        self.msg = "Hello"

d = Demo()
print(d.msg)

#parameterised Constructor
class Demo:
    def __init__(self, message):
        self.msg = message

d = Demo("Hi how are you")
print(d.msg)



#self Keyword
class laptop :
    def __init__(self):
        self.price=""
        self.ram=""
    def display(self):
        print("Laptop is good")
        print(self.price)
        print(self.ram)

hp=laptop()
hp.price=25000
hp.ram="16gb"
hp.display()