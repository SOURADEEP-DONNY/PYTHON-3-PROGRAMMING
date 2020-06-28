# READING A CSV FILE
f=open('PLAYERS.CSV','r')
print(f.read())
f.close()

print('\n\n\n')

#SPLITTING THE CONTENTS OF THE FILES LINE BY LINE
f=open('PLAYERS.CSV','r')
print(f.readlines())
f.close()


print('\n\n\n')

#SPLITTING EACH WORD LINE BY LINE.
with open('PLAYERS.CSV')as p:
    for i in p:
        print(i.strip().split(','))
p.close()
