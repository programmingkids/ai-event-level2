class Person:
    def say_hello(self):
        print("Hello")

    def say_name(self, name):
        print("I am " + name)


person = Person()
person.say_hello()
person.say_name("Bob")
