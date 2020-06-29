#Challenge: Using the file example.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

p_words=[]
k=[]
f=open('example.txt','r')
for i in f:
    k=i.strip().split()
    for j in k:
        if 'p' in j:
            p_words.append(j)
print(p_words)
