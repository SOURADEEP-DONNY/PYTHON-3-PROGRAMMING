def int_return(x):
    return x
print(int_return(27))
def add(_):
    return _+2
print(add(100))
def change(s):
    return s+' Nice to meet you!'
print(change('Donny,'))
def accum(lst):
    s=0
    for i in lst:
        s=s+i
    return s
a=[10,20,30,40,50,60,70,80,90]
print(accum(a))
def length(lst):
    c=0
    for _ in lst:
        c=c+_
    if c>=5:
        return "Longer than 5"
    return "Less than 5"

a=[10,20,90]
print(length(a))
aa=[10,20,90,900,67,80]
print(length(aa))
def divide(x):
    return x//2
def sum(x):
    return (x//2)+6
