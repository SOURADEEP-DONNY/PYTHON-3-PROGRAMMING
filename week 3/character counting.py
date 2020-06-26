#NUMBER OF CHARACTERS IN A STRING(ONLY SPACES WIL BE NEGLECTED)

line="Hey there! life is awesome."
total=0
for _ in line:
    if _ !=' ':
        total=total+1

print('Total characters =',total)
