#NON MUTATING METHODS OF STRINGS
# 1.UPPER METHOD

s='   souradeep is an engineer    '
print(s.upper())

# 2.LOWER METHOD
s2='   SOURADEEP IS AN ENGINEER.   '
SS=s2.lower()
print(SS)


#3. COUNT METHOD
c=s.count('e')
print('THE TOTAL NUMBER OF "e"',c)


#4. STRIP METHOD
print('***'+s.strip()+"***")


#5. REPLACE METHOD
s3=s2.replace('E','@')
print(s3)


#BUT AFTER ALL THESE METHODS THE STRINGS WHICH ARE INITIALIZED EARLIER ARE STILL
#UNALTERED

print(s)
print(s2)
