sentence='India is great. India has the longest democracy in the world.'
words=sentence.split()
words_dict={}
for i in words:
    if i not in words_dict:
        words_dict[i]=0
    words_dict[i]=words_dict[i]+1
print(words_dict)
