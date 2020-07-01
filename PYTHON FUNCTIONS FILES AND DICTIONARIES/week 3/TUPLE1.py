# WE CAN RETURN ONE VALUE IN FUNCTION BUT THAT CAN BE A TUPLE

#HERE IN THE FIRST PROGRAM I AM GOING TO CALCULATE THE AREA AND PERIMETER OF  SQUARE
#--------------TUPLE PACKING------------------------
def square_cal(s):
    a=s*s
    p=4*s
    return (a,p)

s=int(input('\nEnter side of the square:'))
print(square_cal(s))
