#CLONING A LIST
#MAKING EXACT COPY OF A LIST
#BUT THE COPY WILL NOT BE THE EXACT LIST.

list1=["sachin","virat","sourav",7]
list2=list1[:] #CLONING THE LIST 1.

print(list1==list2) #CHECKING WHETHER THE TWO LISTS ARE EQUIVALENT OR NOT.
print(list1 is list2) #CHECKING WHETHER THE TWO LISTS ARE EXACTLY SAME OR NOT.

list1[-1]=' MS.Dhoni'
print(list1==list2)
