class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


customer1 = Person("John", "Doe")
customer2 = Person("Jane", "Doe")
customer3 = Person("Jack", "Doe")

print(customer1.name)
