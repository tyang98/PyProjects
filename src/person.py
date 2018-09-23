"""
Module containing the class: Person

Author: Anne Bracy (awb93)
Date:   Mar 17, 2018
"""

 
class Person():
    """
    A person has a name and can have up to 2 parents.
    
    to create a person:
    kid = family.Person("Adam", None, None) 
    """
    
    def __init__(self, name, parent1, parent2):
        """
        Creates a new Person
        """
        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2
