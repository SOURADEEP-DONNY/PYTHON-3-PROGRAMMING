my_str = "MICHIGAN"
for _ in my_str:
    print(_)

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for _ in several_things:
    print(_)
    
for __ in several_things:
    print(type(__))


str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.
for i in str_list:
    print(len(i))




original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars=0
for j in original_str:
    num_chars=num_chars+1
print(num_chars)




import turtle
s=turtle.Screen()
s.bgcolor("lightgreen")
donny=turtle.Turtle()
donny.color("blue")
for _ in [1,2,3,4]:
    donny.forward(100)
    donny.right(90)
    




lett=""
for i in range(0,7,1):
    lett=lett+'b'
    
print(lett)




addition_str = "2+5+10+20"
k=addition_str.split("+")
sum_val=0
for i in k:
    sum_val=sum_val+int(i)





week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
_=week_temps_f.split(",")
i=0
s=0
avg_temp=0
for __ in _:
    i=i+1
for j in _:
    s=s+float(j)
avg_temp=s/i
print(avg_temp)

