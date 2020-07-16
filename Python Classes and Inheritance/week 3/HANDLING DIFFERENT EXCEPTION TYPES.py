#=============================HANDLING DIFFERENT EXCEPTION TYPES============================

items=['a','b']
try:
    myvar=a
    x=100/0
    third=items[2]
    print('a')
except ZeroDivisionError:  #THIS EXCEPTION HANDLES ANYTHING DIVIDE BY ZERO ERROR.
    print('CANNOT PRINT ANYTHING BY ZERO!!!')
except IndexError:  #THIS EXCEPTION HANDLES ONLY INDEX ERROR.
    print('Index out of bounds')
except Exception: #THIS EXCEPTION HANDLES ANY TYPE OF ERROR.
    print('Something went wrong!!!')

print("THIS DOESN'T RUN")
#=====================================================================================
