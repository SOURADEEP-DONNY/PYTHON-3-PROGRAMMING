#WAP TO STORE THE WORD IN A LIST lst CONTAINING THE LETTER 'S'.

info=[['SOURADEEP','DAS',1997,'KOLKATA'],['SUKLA','DAS',1965,'KOLKATA'],['SATTYAK','SARMA',1997,'DURGAPUR']]
lst=[]

for i in info:
    for j in i:
        j=str(j)  #CONVERTING EVERY ELEMENT INSIDE THE INSIDER LIST TO STRING FOR COMPARISON.

        if 'S' in j:
            lst.append(j)
print(lst)
