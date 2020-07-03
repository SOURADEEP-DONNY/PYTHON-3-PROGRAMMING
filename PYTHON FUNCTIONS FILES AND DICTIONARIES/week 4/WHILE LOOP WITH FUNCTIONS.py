def natural_num_add(limit):
    start=1
    sum_of_nos=0
    while start<=limit:
        sum_of_nos=sum_of_nos+start
        start=start+1
    return sum_of_nos

print('The sum =',natural_num_add(4))
print('The sum =',natural_num_add(1000))
