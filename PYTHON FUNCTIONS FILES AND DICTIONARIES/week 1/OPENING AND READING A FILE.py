#OPENING A FILE IN READ MODE
#READING THE CONTENTS OF THE FILE
#CLOSING THE FILE

#USING EXMPLE.TXT AS A TEXT FILE

f=open('example.txt','r')
contents=f.read()
print(contents[:1000])
f.close()


# PRINTING THE CONTENTS IN THE FORM OF LIST AND THAT LINE BY LINE
ff=open('example.txt','r')
lines=ff.readlines()
print(lines[:3])
ff.close()
