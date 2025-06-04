#Child classes can override methods from parent classes
class Animal:
    def sound(self):
        print("the sound of every animal is different")

class Dog(Animal):
    name="dog"
    def sound(self):    #overriding the method in the animal class
        print(f"{self.name} barks")

d=Dog()
d.sound()