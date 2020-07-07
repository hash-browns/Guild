import unittest
from guidsld import foodOrder

class NamesTestCase(unittest.TestCase):

    def test_acceptance(self):
       self.assertEqual(foodOrder(5,3,7,17), 363.6)

    def test_zero_dogs(self):
       self.assertEqual(foodOrder(0,0,0,0), 0)
       
    #def test_negative_dogs(self)                       ##Covered in input validation dogs.py
       #result = foodOrder(-1,-2,-3,-1)
       #self.assertEqual(result, 0)

    #def test_letters(self):                            ##Covered in input validation in dogs.py
       #self.assertRaises(ValueError, foodOrder('a',12,12,0))

    def test_greater_than_thirty(self):
       result = foodOrder(12,12,12,0)
       self.assertRaises(AssertionError)   
    
    def test_max_dogs(self):
       self.assertEqual(foodOrder(30,0,0,17), 339.6)
       self.assertEqual(foodOrder(0,30,0,17), 699.6)
       self.assertEqual(foodOrder(0,0,30,17), 1059.6)

    def test_surplus_covers_order(self):
       self.assertEqual(foodOrder(0,0,30,900), 0)
