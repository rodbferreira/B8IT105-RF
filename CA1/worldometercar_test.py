# -*- coding: utf-8 -*-
"""
Created on Sat 7 Apr   20:54:37 2020

@author: Rodolfo Laptop
"""

import unittest

import worldometercar 

class TestWorldometercar(unittest.TestCase):

    def setUp(self):
        self.contents = worldometercar.get_page_contents()
        pass

    def test_get_page(self):
        self.assertTrue(len(self.contents) > 0)
        
    def test_conveet_to_soup(self):
        self.assertTrue(worldometercar.convert_to_soup(self.contents) is not None)
        
if __name__ == '__main__':
    unittest.main()