class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")


c = Child()
c.parent_method()  # Inherited from Parent
c.child_method()   # Defined in Child


#TYPES of inheritance
# 1) single inheritance
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()

# 2) Multilevel inheritance
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()


# 3) Multi level inheritance
class Grandparent:
    def house(self):
        print("Big house")

class Parent(Grandparent):
    def car(self):
        print("Family car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

c = Child()
c.house()
c.car()
c.bike()


#4) Hierarchical
class Parent:
    def say(self):
        print("Hello from Parent")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.say()
c2.say()
