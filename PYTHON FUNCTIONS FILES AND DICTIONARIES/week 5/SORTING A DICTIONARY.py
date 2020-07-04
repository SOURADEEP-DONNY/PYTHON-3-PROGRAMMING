#SORING A DICTIONARY
l=['a','x','t','a','r','o','p','e','o','w','r','a','b','c','b','z']
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1

for i in sorted(d.keys()):
    print(i,'\t',d[i])
