#PROGRAM TO ADD AS MANY NUMBERS AS POSSIBLE. TO STOP THE ADDITION ENTER ZERO.
#THIS KIND OF LOOP IS ALSO KNOWN AS LISTENER'S LOOP.
SUM=0
number=1
while number!=0:
    number=int(input('Enter a number to add-'))
    SUM=SUM+number

print('The sum =',SUM)
