#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:20:44 2019

@author: pinchun
"""

import unittest

import myFunc as myF

# unittest is a framework
# TestCase is a class

class TestClass(unittest.TestCase):         # "TestClass" inherits from "unittest.TestCase"
    
    # function names need to start with "test"
    # not necessary to append underline ("test_")
    def test_func1(self):
        
        myInput = 1
        myOutput = myF.increase(myInput)
        expect = 2
        
        self.assertEqual(myOutput, expect)
        
        
        # can have more than one "assert" within one function
        myInput = 10
        myOutput = myF.increase(myInput)
        expect = 11
        
        self.assertEqual(myOutput, expect)
    
    # This won't be tested because the function name does not begin with "test"
    def t_func2(self):
        myInput = 10
        myOutput = myF.increase(myInput)
        expect = 11
        self.assertEqual(myOutput, expect)
    
    def test_func3(self):
        myList = [1,3,6]
        self.assertIn(3, myList)
    
    
    def testFunc4(self):
        
        myInput = 100
        myOutput = myF.decrease(myInput)
        expect = 98     # try the wrong result
                        # if one "assert" in the test function fail, the whole test function will be fail
        self.assertEqual(myOutput, expect)
        
        
        myInput = 100
        myOutput = myF.decrease(myInput)
        expect = 99
        
        self.assertEqual(myOutput, expect)
        
    def testFunc5(self):
        myList = [1,3,6]
        self.assertNotIn(9, myList)
        
    # if there is no assert in the test function
    # the result will always be "." (pass)
    def test_func6(self):
        myList = [1,3,6]


# if there are multiple classes
# all functions with prefix "test" in all classes inheriting "unittest.TestCase" class will be tested
class TestClass2(unittest.TestCase):
    
    def test_func7(self):       # test another wrong case
        
        myInput = 10
        myOutput = myF.increase(myInput)
        expect = 10
        
        self.assertEqual(myOutput, expect)

    def test_func8(self):
        
        myInput = 10
        myOutput = myF.increase(myInput)
        expect = 11
        
        self.assertEqual(myOutput, expect)


if __name__ == '__main__':
    unittest.main()


# python tester.py
# output:
# F....F.          (The sequence of test results seem to be depending on the function names)
# FAIL: testFunc4 (__main__.TestClass)
# FAIL: test_func7 (__main__.TestClass2)
