#DICTIONARY METHODS

#1. PRINTING ALL THE KEYS.
dict1={ 'cricket bats': 500,'footballs': 500,'table tennis balls': 300,'table tennis bats': 300,
        'carrom boards': 100,'badminton bats': 400,'lawn tennis bats': 200,'lawn tennis balls': 800,
        'roller skates': 150}
for i in dict1.keys():
    print(i)


print('\n\n\n')

#2.PRINTING KEYS WITH VALUES.
for j in dict1.keys():
    print(j,'are total of',dict1[j])



print('\n\n\n')

#3.OBTAINING THE LIST OF KEYS
k=list(dict1.keys())
print(k)


print('\n\n\n')


#3. LIST OF KEY VALUE PAIRS IN TERMS OF TUPLES
l=list(dict1.items())
print(l)

print('\n\n\n')

#4. .get()
print(dict1.get('rugby'))
print('\n\n')
print(dict1.get('rugby',0))

print('\n\n')
#BUT ACTUALLY THIS VALUE DOESN'T CHANGE.
print(dict1.get('cricket',1000))


#CRICKET QUANTITY IS NOT CHANGING STILL
for i in dict1.keys():
    print(i,'=',dict1[i])
