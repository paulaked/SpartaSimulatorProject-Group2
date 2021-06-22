import unittest
from random import randint
from script_with_functions import t, new_people
from into_academy import leave_waiting_list
from new_centre import training_academies
from dict_centres import centre


class ProjectTest(unittest.TestCase):
    
        
    def testacademylessthan100(self):
        self.assertLessEqual(training_academies["London"], 100)
        
        
    def testisint(self):
        self.assertIsInstance(t, int)
        
        
    def testnumberofstudents(self):
        self.assertGreaterEqual(new_people, 20)
        self.assertLessEqual(new_people, 30)
        
        
    def testclasssize(self):
        self.assertLessEqual(leave_waiting_list(), 20)
        
        
if __name__ == '__main__':
    unittest.main()