l=[10,20,30,40]
s=sum(l)
print("the sum",s)


new=input("enter the word")
s={}
count=0
for x in new:
    count +=1
    s[x]=s.get(x,0)+1

print(s)
print(count)


def sum(a,b):
    print(a+b)
sum(10,20)


def sumn(*a):
    result=0
    for x in a:
        result=result+x
        print("the result",result)
sumn()
sumn(10,11+20)
sumn(10,20)


