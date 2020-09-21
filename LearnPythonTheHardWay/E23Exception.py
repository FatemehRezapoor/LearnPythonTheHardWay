# July, 8, 2020
# ERROR TRACKING

# CASE 1: In a normal situation, when error happens, the editor shows all the lines which are effected by the error and will not execute the code.
"""
def main1():
    x=int ('foo')
    print('Tadaaaa')

main1()
"""
# Error is : Traceback (most recent call last): File "D:/Repository/LearnPythonTheHardWay/E23Exception.py", line 10, in <module> main() File "D:/Repository/LearnPythonTheHardWay/E23Exception.py", line 7, in mainx=int ('foo')
# ValueError: invalid literal for int() with base 10: 'foo'

# EXPLAINATION: Error happens at line 7, and it is calledd by line 10. Type is ValueError

# CASE 2: What if we want to run the rest of the code?

def main2():
    try:
        x=int ('foo')
    except ValueError:
        print('Value error')
    print('Tadaaaa')

main2()

# As you see it is running the rest of the code

def main3():
    try:
        x=5/0
    except ZeroDivisionError:
        print('Zero error')
    else:
        print('Nice')
    print('Tadaaaa')

main3()

# What if error is not what you guessed?

def main4():
    try:
        x=5/0
    except ValueError:
        print('Value error')
    except:
        print('Unknown error')
    print('Tadaaaa')

main4()

# TO KNOW MORE ABOUT ERROR:
import sys
def main5():
    try:
        x=5/0
    except ValueError:
        print('Value error')
    except:
        print('Unknown error: {}'.format(sys.exc_info())) # FIND ERROR TYPE
    print('Tadaaaa')

main5()