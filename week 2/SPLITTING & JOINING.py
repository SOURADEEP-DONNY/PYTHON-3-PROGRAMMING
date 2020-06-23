#SPLITTING & JOINING STRING

# SPLIT FUNCTION GENERALLY SPLITS A STRING AND CUTS IT FROM THE SPACES WHEN
# THERE IS NO ARGUMENT IS BEING PASSED.

A="INDIA IS GREAT!"
k=A.split()
print(k)


# WHEN ARGUMENT IS PASSED.

a="love/leader/long/&/last!"
k=a.split('/')
print(k)



a="RONALDO;PELE;MARADONA;MESSI;BEBETO;FEDEX"
k=a.split(';')
print(k)


# JOINING A LIST INTO STRING
l=['INDIA','IS','GREAT']
S='-'.join(l)
print("\n\n"+S)
