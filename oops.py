# OOP -> Object oriented programming for python

# attr_1 = "xyz"
# attr_2 = "abc"
# print(attr_1 + attr_2)

# Reusability of program was not possible without oop
# Accidental value update is possible without oop
# The code becomes big if oop implemented

# Types of OOPS
# 1. class
# 2. object
# 3. Inheritance
# 4. Polymorphism
# 5. Encapsulation
# 6. Abstraction

# class: A class used to create objects.
#        Blueprint of of an objects.
#        A class has attributes and methods -> attributes ==  class variable, methods == functions
#        A class has its own identity and behaviour -> identity == name, behaviour == methods

class Students:
    cls_strength = 10

    def display(self):
        return(Students.cls_strength)


# object: Instance of a class
#         An object has its own identity, behaviour and state -> object attributes

# class Students:
#     cls_strength = 10
#
#     def display(self):
#         print(self.cls_strength)
#         return(self.cls_strength)
#
# student_obj = Students()
# test_return = student_obj.display()

# Inheritance: It allows to inherit property and method of parent class into child class
            #   Single Inheritance -> 1 child class and 1 Parent class
            #   Multiple Inheritance -> 1 child class and more than 1 Parent class
            #   Multilevel Inheritance -> 1 child class inherit property and method of
#                                         its parent class which inherits  property and method of their parent class
            #   Hierarchiel Inheritance -> more than 1 child class is inhering property of a single parent class.
            #   Hybrid Inheritance -> combination of multilevel inheritance and Hierarchiel

# ------------ Single Inheritance

class Students:
    cls_strength = 10

    def display(self):
        print(self.cls_strength)
        # return(self.cls_strength)

class Batch(Students):
    def display(self):
        print(f"This is python batch with strength of {self.cls_strength}")


batch_obj = Batch()
batch_obj.display()

# ----------------Multiple Inheritance-----------

class Guvi:
    def _guvi(self):
        print("We are attending Guvi classes")

class Course():
    def _course(self):
        print("We are from Python Automation testing")

class Batch(Guvi,Course):
    def _batch(self):
        print("We are in batch B4")

student = Batch()
student._guvi()
student._course()
student._batch()



# ------------ Mutlilevel Inheritance-------------

class Guvi:
    def _guvi(self):
        print("We are attending Guvi classes")

class Course(Guvi):
    def _course(self):
        print("We are from Python Automation testing")

class Batch(Course):
    def _batch(self):
        print("We are in batch B4")

student = Batch()
student._guvi()
student._course()
student._batch()


# Polymorphism : A child class can have same method name but different implementation than its parent class

class Bird:
    def show(self):
        print("Birds can fly")

class Ostrich(Bird):
    def show(self):
        print('Ostrich cannot fly')

class Sparrow(Ostrich):
    def show(self):
        print('Sparrow are small')

bird_obj = Sparrow()
bird_obj.show()

#       Encapsulation: This is wrapping of methods and attributes inside a class.
#                         __attr1 -> Private variable
#                          _attr2 -> Protected variable
#                           attr3 -> Public variable

# class Students:
#     __cls_strength = 10
#
#     def display(self):
#         print(self.__cls_strength)
#         # return(self.cls_strength)
#
# class Batch(Students):
#     def display(self):
#         print(f"This is python batch with strength of {self.__cls_strength}")
#
#
# batch_obj = Batch()
# batch_obj.display()

#                Abstraction: This is used for hiding implementation of a method or any functionality

from abc import  ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def show(self):
        pass

class B:
    def show(self):
        print('Hello')

obj = B()
obj.show()


