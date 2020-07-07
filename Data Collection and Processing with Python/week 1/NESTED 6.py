#------------------------DEEP COPIES-----------------------------------
#-------------------------------------------------------------------------
#ALIASING IN NESTED LISTS.

original=[['FOOTBALL','CRICKET','TABLE TENNIS','HOCKEY'],['PHYSICS','MATHEMATICS','COMPUTER SCIENCE','ENVIRONMENTAL SCIENCE']]
copied_outer=[]
for i in original:
    copied_inner=[]
    for j in i:
        copied_inner.append(j)
    copied_outer.append(copied_inner)

print(copied_outer)

#APPENDING ELEMENTS IN ORIGINAL LIST.
original.append('[chess]')

print('\n')
#PRINTING THE ORIGINAL LIST.
print('ORIGINAL LIST =',original)

print('\n')
#PRINTING THE COPIED VERSION
print('COPIED VERSION=',copied_outer)
