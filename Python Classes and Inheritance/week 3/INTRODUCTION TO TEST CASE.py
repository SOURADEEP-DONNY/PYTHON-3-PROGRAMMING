#========================INTRODUCTION TO TEST CASES==============================
#================================================================================
def square(x):
    return x*x

import test
print('TESTING SQUARE FUNCTION')
test.testEqual(square(10), 100)
