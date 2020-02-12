class Person:
    def say_name(self):
        print("I am " + self.name)

    def say_age(self):
        print("I am " + str(self.age) + " years old")


person = Person()
person.name = "Ariel"
person.age = 17
person.say_name()
person.say_age()
