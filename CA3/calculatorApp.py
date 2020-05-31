'''
Rodolfo Ferreira
Programming for Big Data
Id 10540987
CA3 - 10 Functional Calculator with Map Reduce Filter & Generator
'''

from functools import reduce

from calculator import Calculator

class CalculatorApp():
 
 
    def menu(self):
            print('#'*45)
            print('''DBS Calculator
            
            Please choose one of the follow options:
            
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Get Max
            5. Get Min
            6. Cube
            7. Square
            8. Convert Kilograms to Pounds
            9. Convert Pounds to Kilograms
            10. Convert Temperature Celsius to Fahrenheith
            11. Convert Temperature Fahreheith to Celsius
            ''')
            print('#'*45)
    
    def run_choice(self):
        print('# After every number press Enter. Press = to do the calculation')
        numbers = ''
        numbers_list = []
        while numbers != '=':
            numbers = input('Enter Number: ')
            if numbers != '=':
                numbers_list.append(float(numbers))
        return numbers_list

        
    def process_calculation(self):
        self.menu()
         # Take input from the user 
        choice = input("Enter choice(1 to 11) or 'e' to Exit: ")
         
        if choice not in ('1','2','3','4','5','6','7','8','9','10','11','e') :
            print("Invalid input")
        
        elif choice == 'e':
            print('')
            
        
        elif choice == '1':
            print('# Chosen operation = Addition')
            numbers_list = []
            numbers_list = self.run_choice()
            if len(numbers_list) > 1:
                print("Result = ", Calculator().addition(numbers_list))
                            
        elif choice == '2':
            print('Chosen operation = Subtraction')
            numbers_list = []
            numbers_list = self.run_choice()
            if len(numbers_list) > 1:
                print("Result = ", Calculator().subtraction(numbers_list))
    
        elif choice == '3':
            print('Chosen operation = Multiplication')
            numbers_list = []
            numbers_list = self.run_choice()
            if len(numbers_list) > 1:
                print("Result = ", Calculator().multiplication(numbers_list))
                
        elif choice == '4':
            print('Chosen operation = Get Max')
            numbers_list = []
            numbers_list = self.run_choice()                    
            if len(numbers_list) > 1:
                print("Result = ", Calculator().max(numbers_list))
                
        elif choice == '5':
            print('Chosen operation = Get Min')
            numbers_list = []
            numbers_list = self.run_choice()                            
            if len(numbers_list) > 1:
                print("Result = ", Calculator().min(numbers_list))
                
        elif choice == '6':
            print('Chosen operation = Cube')
            numbers_list = []
            numbers_list = self.run_choice()    
            if len(numbers_list) > 0:
                print("Result = ", Calculator().cube(numbers_list))
                
        elif choice == '7':
            print('Chosen operation = Square')
            numbers_list = []
            numbers_list = self.run_choice()
            if len(numbers_list) > 0:
                print("Result = ", Calculator().square(numbers_list))
                
        elif choice == '8':
            print('Chosen operation = Convert Kilograms to Pounds')
            numbers_list = []
            numbers_list = self.run_choice()   
            if len(numbers_list) > 0:
                print("Result = ", Calculator().kg_to_pound(numbers_list))
                
        elif choice == '9':
            print('Chosen operation = Convert Pounds to Kilograms')
            numbers_list = []
            numbers_list = self.run_choice()   
            if len(numbers_list) > 0:
                print("Result = ", Calculator().pound_to_kg(numbers_list))  
    
        elif choice == '10':
            print('Chosen operation = Convert Celsius to Fahrenheith')
            numbers_list = []
            numbers_list = self.run_choice()     
            if len(numbers_list) > 0:
                print("Result = ", Calculator().celsius_to_fahren(numbers_list))
                
        elif choice == '11':
            print('Chosen operation = Convert Fahrenheit to Celsius')
            numbers_list = []
            numbers_list = self.run_choice()     
            if len(numbers_list) > 0:
                print("Result = ", Calculator().fahren_to_celsius(numbers_list))
                  
    def process(self):
        go_again = ''
        while go_again != 'n':
            self.process_calculation()
            print('')
            print("Would you like to do another calculation?")
            go_again = input("Press any key to continue or 'n' to Exit: ")
            print('See you around, be safe!')
    


if __name__ == "__main__":
    obj = CalculatorApp()
    obj.process()
    
