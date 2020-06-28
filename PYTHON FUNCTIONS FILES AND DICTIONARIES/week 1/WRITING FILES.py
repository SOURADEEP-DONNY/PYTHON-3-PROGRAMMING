f=open('files.txt','w')
f.write('SQUARES OF FIRST 10 WHOLE NUMBERS')
for i in range(10):
    sq=i**2
    f.write(str(sq))
    f.write('\n')
f.close()
