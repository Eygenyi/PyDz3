import random
n=int(input('input length: '))
l=[]
for i in range(n):
    l.append(random.randint(1,20))
    print(l[i],end='  ')
f=int(input('\ninput number : '))
min=l[0]
for j in l:
        if abs(j-f)<abs(min-f):
            min=j
print('nearly element:=',min)