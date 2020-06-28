#WRITING A CSV FILE

name=""
stream=""
yop=""
f=open('data.csv','w')
header=f.write('NAME,STREAM,YEAR OF PASSING')
f.write("\n")
for i in range(5):
    f.write(input(f"ENTER NAME:- {name},ENTER STREAM:-{stream},ENTER YEAR OF PASSING:-{yop}"))
    f.write("\n")
f.close()
