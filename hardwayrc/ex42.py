## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## self has-a attribute named name, set that to the parameter name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## self has-a attribute named name, set that to the parameter name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## self has-a attribute named name, set that to the parameter name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employe is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## fancy way of calling this __init__. the superclass has-a Employee
        ## (and self); it also has-a __init__, and call that. also a zillion
        ## times less messy in Python 3
        super(Employee, self).__init__(name)
        ## self has-a salary, set it to salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat (well, duh)
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet, set to satan
mary.pet = satan

## frank is-a Employee with parameters Frank and 120000
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish, which, sigh...
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut, and likes alliteration
harry = Halibut()
