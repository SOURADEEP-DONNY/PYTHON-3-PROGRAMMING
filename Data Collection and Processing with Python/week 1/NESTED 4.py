#WAP TO STORE AND PRINT THE ELEMENTS OF AN INSIDER LIST IN A LIST NAMED lst.

info=[1,2,['Souradeep','Sukla','Arup','Abhinandan'],3,4,5,['Kolkata','West Bengal','India'],6]
lst=[]
list_of_lists=[]
for i in info:
    if type(i) is list:
        list_of_lists.append(i)
        for j in i:
            lst.append(j) #ELEMENTS IN AN INSIDER LIST IN A COMPLETE DIFFERENT LIST ALL TOEGTHER.

print('DIFFERENT LIST =',lst)
print('LIST OF LISTS =',list_of_lists)
        
