#DICTIONARY OPERATIONS

foods={'mutton biriyani':100,'chicken biriyani':125,'cutlet':200,'fish fingers':800}

#DELETE OPERATION
del foods['cutlet']
print(foods)


print('\n\n')

#UPDATING A KEY VALUE PAIR
foods['mutton biriyani'] = 80
print(foods)


foods['fish fingers']=foods['fish fingers']+200
print(foods)

#LENGTH FUNCTION REURNS THE NUMBER OF KEY VALUE PAIRS IN THE DICTIONARY.
length_of_foods=len(foods)
print(length_of_foods)
