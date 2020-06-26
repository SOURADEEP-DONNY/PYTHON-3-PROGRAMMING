list1=[10,20,30]
list2=[10,20,30]

#CHECKING WHETHER THE TWO LISTS ARE SAME OR NOT.
print(list1 is list2)


#CHECKING THE IDS OF THE TWO LISTS.
print('THE ID OF list1 is',id(list1))
print('THE ID OF list2 is',id(list2))

#CHECKING WHETHER THE LISTS ARE EQUIVALENT OR NOT.
print(list1==list2)


#--------ALIASING----------
list1=list2

#AGAIN CHECKING THE IDS OF THE TWO LISTS.
print('THE ID OF list1 is',id(list1))
print('THE ID OF list2 is',id(list2))

#AGAIN CHECKING WHETHER THE TWO LISTS ARE SAME OR NOT.
print(list1 is list2)

#AGAIN CHECKING WHETHER THE LISTS ARE EQUIVALENT OR NOT.
print(list1==list2)
