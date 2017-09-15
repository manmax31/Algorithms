# https://www.interviewbit.com/search/?q%5B%5D=Amazon
# http://www.geeksforgeeks.org/tag/amazon/


def transpose(M):
    """
    Unzip matrix M to get individual rows, then zip those rows to get transpose
    :param M: matrix
    :return:
    """
    return list(zip(*M))
print(transpose([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]))



"""
Ternary Operators
[on_true] if [expression] else [on_false]
"""
print("\nTernary Operators")
min_ = lambda a, b: a if a < b else b
print((min_(4, 3)))



"""
Partial Function
"""
print("\nPartial Function:")
from functools import partial
def add(a,b,c):
    return 100 * a + 10 * b + c

add_part = partial(add, c=2, b=1)
print(add_part(3))



"""
Unpacking
* : tuples, **: dictionaries
"""
print('\nUnpacking:')
def fun(a, b, c, d):
    print(a, b, c, d)

fun(*[1, 2, 3, 4])
fun(*[(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
fun(**{'a': 1, 'b': 2, 'c': 3, 'd': 4})



"""
Packing:
When we don’t know how many arguments need to be passed to a python function, we can use Packing to pack all arguments in a tuple.
"""
print('\nPacking:')
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum
# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))


"""
Any: Returns true if any of the items is True. It returns False if empty or all are false. OR operation
All: Returns true if all of the items are True (or if the iterable is empty). AND operation
"""
print('\nAny:')
print(any([False, False, False, False]))
print(any([False, True, False, False]))
print('\nAll:')
print(all([True, True, True, True]))
print(all([False, True, True, False]))



"""
Counter
"""
print('\nCounter:')
from collections import Counter
coun = Counter()

coun.update([1, 2, 3, 1, 2, 1, 1, 2])
print(coun)
coun.update([1, 2, 4])
print(coun)
print('Most Common: ', coun.most_common(3))


"""
Generator
"""


# A Python program to demonstrate use of
# generator object with next()

# A generator function
print('\nGenerator:')
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.__next__())  # In Python 3, __next__()
print(x.__next__())
print(x.__next__())


"""
Strings
"""
print('\nStrings:')
str = "I am a good boy am"
print(str.find('am'))  # First Occurence of a String
print(str.rfind('am')) # Last Occurence of a String


"""
String Tempaltes
"""
print('\nString Tempaltes:')
# A Python program to demonstrate working of string template
from string import Template

# List Student stores the name and marks of three students
Student = [('Ram', 90), ('Ankit', 78), ('Bob', 92)]

# We are creating a basic structure to print the name and
# marks of the students.
t = Template('Hi $name, you have got $marks marks')

for i in Student:
    print(t.substitute(name=i[0], marks=i[1]))