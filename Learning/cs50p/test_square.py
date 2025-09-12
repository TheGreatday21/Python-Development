#this is a program to unit test the square funciton in my squareFunction file 

from squareFunction import square
#importing the square function from the file 

import pytest

def main():
    #test_square()
    test_negative()
    test_positive()
    test_zero()

#def test_square(): #instead of using one function to test all the code we are going to use two other function to handle all the exceptions in the code 
    #we are going to use the assert function . It returns a boolean expression when something is false 
    #if the code doesnt work we get an assertion error 

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

'''
=============================== test session starts ================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\Elijah\languages_practice\Python\Learning\cs50p
collected 3 items                                                                   

test_square.py FF.                                                            [100%]

===================================== FAILURES =====================================
__________________________________ test_positive ___________________________________

    def test_positive():
        assert square(2) == 4
>       assert square(3) == 9
E       assert 6 == 9
E        +  where 6 = square(3)

test_square.py:18: AssertionError
__________________________________ test_negative ___________________________________ 

    def test_negative():
>       assert square(-2) == 4
E       assert -4 == 4
E        +  where -4 = square(-2)

test_square.py:20: AssertionError
============================= short test summary info ============================== 
FAILED test_square.py::test_positive - assert 6 == 9
FAILED test_square.py::test_negative - assert -4 == 4
=========================== 2 failed, 1 passed in 0.47s ============================

'''
#this is the error we get 

#creating a function to test if a user inputs in a string 
def test_str():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == "__main__":
    main()