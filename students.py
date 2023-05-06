# objects have attributes and behaivours/methods
# an object can be any real world  that can represent in a software program


# creating objects
# to create objects in python, we first define a class.
# we use the class keywoard to create obejcts
# classes will contain objects and methods
# a class just defines the attributes and 
# behaivours of an obejct but it does not actually create an object

# to create an object u instantiate an object


# class methods
# we use methods to add behaivour to a class
# methods are defined as python functions inside the 
     




# Instant variables allow us to create instances of 
# a class where each instance has its own value


# 1) Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
            #  - show_full_name
            #  - year_of_birth
            #  - show_initials


class Student:
    school="AKiraChix"
    

    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def greet_student(self):
         return f"Hello {self.name} from {self.country} welcome to {self.school}"
    def show_fullnames(self):
        return f' {self.first_name + ""} {self.last_name}'
    def year_of_birth(self):
        return 2023 - {self.age} 
    def show_initials(self):
        return {self.first_name[0] }+ "" +{self.last_name[0]}






