word_dict={}
f=open('example2.txt','r')
txt=f.read()
for i in txt:
    if i not in word_dict:
        word_dict[i]=0
    word_dict[i]=word_dict[i]+1
print('TOTAL NUMBER OF i is', word_dict["i"])
print('TOTAL NUMBER OF o is', word_dict["o"])
print('TOTAL NUMBER OF l is', word_dict["l"])
print('TOTAL NUMBER OF I is', word_dict["I"])
