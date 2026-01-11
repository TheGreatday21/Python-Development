##the proper way to document your functions 

#its the one of using ''' Praise the Lord''' or """ Iam a the head and not the tail"""

"""
Python is cool
#this below is generally how you would document a function 

:param n: Number of times iterated
:type n: int
:raise TypeError: if n is not an int
:return : A string of n meows one perline
:rtype :str
"""

def add(num1:int,num2:int) -> int:
    """
    This returns a sum of two numbers 

    :param num1:First number
    :param num2:Second number
    :type num1,num2 : int
    :raise TypeError:if num1 and num2 are not integers
    :return : An integer sum of num1 and num2
    :rtype : int
    """
    return num1 + num2


summation:int = add(23,67)
print(summation)



















