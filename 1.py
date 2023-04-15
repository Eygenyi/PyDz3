import random
n=int(input('input length: '))
l=[]
i=0
count=0
for i in range(n):
    l.append(random.randint(1,5))
    print(l[i],end='  ')
f=int(input('\ninput number : '))
for i in range(n):
    if f == l[i]:
        count+=1
print('=>  ',count)