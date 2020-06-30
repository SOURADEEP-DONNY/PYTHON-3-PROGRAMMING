f=open('example.txt','r')
i_count=0
i_occur=f.read()
for _ in i_occur:
    if _=='i'or'I':
        i_count=i_count+1
print('i occurence is',i_count)
