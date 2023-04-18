diction={1:'AEIOULNSTR'+'АВЕИНОРСТ',2:'DG'+'ДКЛМПУ',3:'BCMP'+'БГЁЬЯ',4:'FHVWY'+'ЙЫ',5:'K'+'ЖЗХЦЧ',8:'JX'+'ШЭЮ',10:'QZ'+'ФЩЪ'}
f=str(input())
count=0
for i in diction:
    for j in f.upper():
        if j in diction[i]:
            count=count+i
print(count)