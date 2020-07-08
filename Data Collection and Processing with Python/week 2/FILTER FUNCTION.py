#------------------------FILTER FUNCTION----------------------------
#-------------------------------------------------------------------
#THE FIRST PARAMETER OF A FILTER FUNCTION IS THE CONDITION IN THE FORM OF LAMBDA
#EXPRESSION FOR SHORTER AND SIMPLIER.

#OR

#A FUNCTION CAN ALSO BE USED WHOSE RETURNING BOOLEAN VALUE IS PASSED AS THE FIRST
#PARAMETER AND THE SECOND PARAMETER IS THE LIST,TUPLE OR THE STRING DATA ITSELF.


lst=[12,33,11,3,21,26,90,87,99,990,1678,1,3334]
new_list=list(filter(lambda i:i%2==0,lst))
print(new_list)

print('\n\n')
#SAME CODING CAN BE DONE BY CREATING A FUNCTION.

def picking_even(i):
    return i%2==0

lst=[12,33,11,3,21,26,90,87,99,990,1678,1,3334]
new_list=list(filter(picking_even,lst))
print(new_list)
