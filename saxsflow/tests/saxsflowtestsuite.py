import unittest
'''
Created on 9 Mar 2015

@author: ademaria
'''
from saxsflow.tests import TestSaxsDataSet

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestSaxsDataSet('testSubtractions'))
    unittest.TextTestRunner().run(suite)
