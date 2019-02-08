l=[]
l1=[]
print("enter size of the list 1 and list 2")
x1=int(input())
x2=int(input())
for i in range(x1):
    y1=input("enter names: ")
    l.append(y1)
print(l)
for i in range(x2):
    y2=input("enter their age: ")
    l1.append(y2)
print(l1)
d=dict(zip(l, l1))
print(d)
