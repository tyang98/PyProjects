"""
Module to demonstrate the Person Class

Author: Anne Bracy (awb93)
Date:   March 17, 2018
"""
import person

shmi = person.Person("Shmi Skywalker", None, None)
anakin = person.Person("Anakin Skywalker", shmi, None)
padme = person.Person("Padme Amidala", None, None)
leia = person.Person("Leia Organa", anakin, padme)
han = person.Person("Han Solo", None, None)
ben = person.Person("Ben/Kylo Ren", leia, han)

def all_ancestors(p):
    print(p.name)
    if not p.parent1 == None:
        all_ancestors(p.parent1)
    if not p.parent2 == None:
        all_ancestors(p.parent2)


def num_ancestors(p):
    """Returns: num of known ancestors
    Pre: p is a Person"""
    # 1 Base case.   
    if p.parent1 == None and p.parent2 == None:        
        return 0

    # 2. Break into two parts    
    parent1s = 0    
    if p.parent1 != None:        
        parent1s = 1+num_ancestors(p.parent1)    
    parent2s = 0    
    if p.parent2 != None:       
        parent2s = 1+num_ancestors(p.parent2)    

    # 3. Combine the result    
    return parent1s+parent2s

all_ancestors(leia)
print("total ancestors = "+str(num_ancestors(leia)))