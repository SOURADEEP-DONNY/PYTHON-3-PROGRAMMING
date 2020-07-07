#ALIASING IN NESTED LISTS.

original=[['FOOTBALL','CRICKET','TABLE TENNIS','HOCKEY'],['PHYSICS','MATHEMATICS','COMPUTER SCIENCE','ENVIRONMENTAL SCIENCE']]
copied=[]
copied=original[:]
print(copied)

#OBJECTS ARE DIFFERENT IN BOTH THE LISTS.
print(original is copied)


#CONTENTS ARE SAME OF THE LISTS
print(original == copied)


#APPENDING IN ORIGINAL LIST.
original[0].append(['chess'])

print('\n\n')

print('ORIGINAL LIST=',original)
print('\n\n')
print('COPIED LIST=',copied)


#BOTH THE LISTS ARE CONTAINING THE SAME ADDED ELEMENT.
