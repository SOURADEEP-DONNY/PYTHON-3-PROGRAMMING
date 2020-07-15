#EXCEPTION HANDLING FLOW OF CONTROL 2.
#=========================================================================================================
item=['a','b','c']
try:
    print('a')  #THIS WAS EXECUTED.
    k=item[2]   #NOW EVERYTHING IS CORRECT.
    print('b')  #THIS WILL ALSO BE EXECUTED.
except:
    print('Something went wrong.')         #SINCE NOTHING WENT WRONG, THE EXCEPT BLOCK WILL NEVER EXECUTE.
    k=False
print('I WANT THIS TO RUN.') # DIRECTLY JUMPS HERE.
#==========================================================================================================
