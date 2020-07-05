
# 1. ADVANCED SORTING
f=['mango','banana','lichu','peach','apple','tomato','carrot','pineapple','berry']
#SORTING ACCORDING TO LENGTH
new_f=sorted(f, key=lambda x:(len(x),x))
print('SORTED ORDER\n\n\n')
for i in new_f:
    print(i)

print('\n\n')
#2. REVERSED SORTING OF THE SAME

f=['mango','banana','lichu','peach','apple','tomato','carrot','pineapple','berry']
#SORTING ACCORDING TO LENGTH
new_f=sorted(f, key=lambda x:(len(x),x),reverse=True)
print('REVERSE SORTED ORDER\n\n\n')
for i in new_f:
    print(i)
