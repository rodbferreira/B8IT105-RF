'''
Rodolfo Ferreira
Programming for Big Data
Id 10540987
CA3 - 10 Functional Calculator with Map Reduce Filter & Generator
github: https://github.com/rodbferreira/B8IT105-RF
'''

import unittest

from calculator import *

sequence1 = [10, 5, 4.5, 0.5, 10]
sequence2 = [-10, 5, 4.5, 0.5, 10]
sequence3 = [10,8]

class TestCalculator(unittest.TestCase):

    def testAddition(self):
        self.assertEqual(30, Calculator().addition(sequence1))
        self.assertEqual(10, Calculator().addition(sequence2))
        self.assertEqual(18, Calculator().addition(sequence3))
        
    def testSubtraction(self):
        self.assertEqual(-10, Calculator().subtraction(sequence1))
        self.assertEqual(-30, Calculator().subtraction(sequence2))
        self.assertEqual(2, Calculator().subtraction(sequence3))
    
    def testMultiplication(self):
        self.assertEqual(1125, Calculator().multiplication(sequence1))
        self.assertEqual(-1125, Calculator().multiplication(sequence2))
        self.assertEqual(80, Calculator().multiplication(sequence3))
    
    def testMax(self):
        self.assertEqual(10, Calculator().max(sequence1))
        self.assertEqual(10, Calculator().max(sequence2))
        self.assertEqual(10, Calculator().max(sequence3))

    def testMin(self):
        self.assertEqual(0.5, Calculator().min(sequence1))
        self.assertEqual(-10, Calculator().min(sequence2))
        self.assertEqual(8, Calculator().min(sequence3))
    
    def testCube(self):
        self.assertEqual([1000,125,91.125,0.125,1000], Calculator().cube(sequence1))
        self.assertEqual([-1000,125,91.125,0.125,1000], Calculator().cube(sequence2))
        self.assertEqual([1000,512], Calculator().cube(sequence3))
    
    def testSquare(self):
        self.assertEqual([100,25,20.25,0.25,100], Calculator().square(sequence1))
        self.assertEqual([100,25,20.25,0.25,100], Calculator().square(sequence2))
        self.assertEqual([100,64], Calculator().square(sequence3))
    
    
    def testKg_to_pound(self):
        self.assertEqual([22.061999999999998, 11.030999999999999, 9.9279, 1.1031, 22.061999999999998], Calculator().kg_to_pound(sequence1))
        self.assertEqual([-22.061999999999998, 11.030999999999999, 9.9279, 1.1031, 22.061999999999998], Calculator().kg_to_pound(sequence2))
        self.assertEqual([22.061999999999998,17.6496], Calculator().kg_to_pound(sequence3))
    
    def testPound_to_kg(self):
        self.assertEqual([4.532680627322999, 2.2663403136614995, 2.0397062822953496, 0.22663403136614996, 4.532680627322999], Calculator().pound_to_kg(sequence1))
        self.assertEqual([-4.532680627322999, 2.2663403136614995, 2.0397062822953496, 0.22663403136614996, 4.532680627322999], Calculator().pound_to_kg(sequence2))
        self.assertEqual([4.532680627322999,3.6261445018583993], Calculator().pound_to_kg(sequence3))
    
    def testCelsius_to_fahren(self):
        self.assertEqual([50.0, 41.0, 40.1, 32.9, 50.0], Calculator().celsius_to_fahren(sequence1))
        self.assertEqual([14, 41.0, 40.1, 32.9, 50.0], Calculator().celsius_to_fahren(sequence2))
        self.assertEqual([50,46.4], Calculator().celsius_to_fahren(sequence3))
    
    def testFahren_to_celsius(self):
        self.assertEqual([-12.222222222222223, -15.0, -15.277777777777779, -17.5, -12.222222222222223], Calculator().fahren_to_celsius(sequence1))
        self.assertEqual([-23.333333333333336, -15.0, -15.277777777777779, -17.5, -12.222222222222223], Calculator().fahren_to_celsius(sequence2))
        self.assertEqual([-12.222222222222223,-13.333333333333334], Calculator().fahren_to_celsius(sequence3))


unittest.main()