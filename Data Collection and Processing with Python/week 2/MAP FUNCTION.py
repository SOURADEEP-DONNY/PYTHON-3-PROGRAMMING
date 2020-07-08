#-------------------------------MAP FUNCTION---------------------------------
#----------------------------------------------------------------------------
#MAP FUNCTION TAKES ONE INPUT AS A FUNCTION (1st input)WHERE
#THE FUNCTION ITSELF TAKES ONE INPUT AND RETURNS THE REQUIRED OUTPUT.

names=['souradeep', 'ayusha', 'donny', 'diya']

def the_function(st):
    return st.upper()  # HERE WE ARE RETURNING THE UPPER CASE OF THE GIVEN STRING INPUTS.

UPPER_NAMES=list(map(the_function,names))
print(UPPER_NAMES)

print('\n\n')
print('SAME OUTPUT')
print('\n')

#IT'S NOT ALWAYS THE CASE TO USE A FUNCTION WE CAN ALSO USE LAMBDA EXPRESSIONS
#AS THE FIRST INPUT OF THE MA FUNCTION IS AS WELL

#SAME CODE USING LAMBDA EXPRESSION

names=['souradeep', 'ayusha', 'donny', 'diya']
UPPER_NAMES=list(map(lambda string: string.upper(),names))
print(UPPER_NAMES)

#USING LAMBDA EXPRESSIONS MAKE THE CODE EVEN SHORTER AND SIMPLER.
