#EXCEPTION HANDLING FLOW OF CONTROL.
#===============================================================================
item=['a','b']
try:
    print('a')  #THIS WAS EXECUTED.
    k=item[2]   #THIS PROVOKED A RUNTIME ERROR HENCE THE NEXT STATEMENT WON'T RUN.
    print('b')  #THIS WAS NEVER EXECUTED.
except:
    print('Something went wrong.')         #INTERPRETER JUMPED TO THIS LINE.
    k=False
print('I WANT THIS TO RUN.')
#================================================================================
