import unittest
import time_function


class ProjectTest(unittest.TestCase):
    
        
    def testacademylessthan100(self):
        self.assertLessEqual(len(time_function.in_training), 100)
        
        
    def testisint(self):
        self.assertIsInstance(int(time_function.t), int)
        
        
    def testnumberofstudents(self):
        self.assertGreaterEqual(21, 20)
        self.assertLessEqual(21, 30)
        
        
    def testclasssize(self):
        self.assertLessEqual(15, 20)
        
        
if __name__ == '__main__':
    unittest.main()