'''
Rodolfo Ferreira
Programming for Big Data
Id 10540987
CA3 - 10 Functional Calculator with Map Reduce Filter & Generator
'''


from functools import reduce

class Calculator():
    
    def __init__(self):
        self.choice = 0
        self.values = []
       
    # This function does addition from a list of numbers
    def addition(self, values):
        return reduce(lambda x, y: x + y, values)
    
    # # This function does subtraction from a list of numbers
    def subtraction(self, values):
        return reduce(lambda x, y: x - y, values)
    
    # This function does multiplication from a list of numbers
    def multiplication(self, values):
        return reduce(lambda x, y: x * y, values)
    
    # This function gets the max number from a list of numbers
    def max(self, values):
        return reduce(lambda a,b: a if (a>b) else b, values) 
    
    # This function gets the min number from a list of numbers
    def min(self, values):
        return reduce(lambda a,b: a if (a<b) else b, values)     
   
    # This function cubes every number in a list
    def cube(self, values):
        return list(map(lambda x: x ** 3, values))
    
    # This function squares every number in a list
    def square(self, values):
        return list(map(lambda x : x*x, values))
    
    # This function converts a list of numbers from Kg into Pounds
    def kg_to_pound(self, values):
        return [(x * 2.2062) for x in values]
    
    # This function converts a list of numbers from Pounds into Kg
    def pound_to_kg(self, values):
        return [(x / 2.2062) for x in values]
    
    # This function converts a list of numbers from celsius into fahrenheith      
    def celsius_to_fahren(self, values):
        return [((float(9) / 5) * x + 32) for x in values ]

     # This function converts a list of numbers from Pounds into Kg
    def fahren_to_celsius(self, values):
        return [(x - 32) * float((5) / 9) for x in values ]

