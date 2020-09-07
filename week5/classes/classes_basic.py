# Classes - Chapter 9
# Class - general template, where you have description and behaviour anything you wanted to represent
# class name always starts with capital letter

class Dog():
    """This is the general class about Dog."""
    # Attribute(properties)
    breed = ''
    name = ''

    # Behaviour, methods
    def bark(self):
        print("wouf wouf!!")

# Object is the instance(representation in specific way) of class
mydog = Dog()  # mydog is the object of Dog() class
mydog.breed = 'German shepard'
mydog.name = 'Rex'
mydog.bark()

yourdog = Dog()
yourdog.name = "Bobik"
yourdog.breed = 'pudo'
yourdog.bark()