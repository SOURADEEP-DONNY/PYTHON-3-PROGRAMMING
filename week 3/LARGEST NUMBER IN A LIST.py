#LARGEST NUMBER IN A LIST

a=[100,200,300,400,500,600,2,5,1,999,800,567]
largest_number=a[0]
for i in a:
    if i>a[0]:
        a[0]=i

print('The largest number is',a[0])
