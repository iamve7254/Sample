l=[10,12,14,11,15,78]
s=list(filter(lambda x:x%2==0 ,l))
print(s)
s1=list(filter(lambda x:x%2!=0 ,l))
print(s1)


def evela(x):
    if x%2==0:            #onely true or false
        return  True
    else:
        return False
l = [100, 102, 4, 11, 15, 78]
s = list(filter( evela, l))
print(s)


l=[1,2,3,45,5]
s=list(map(lambda x:2*x,l))                      #any type
print(s)


a=[1,20,3,4]
a1=[4,5,40,80,45,47]
snew=list(map(lambda x,y:x*y,a,a1))           #multiple list values
print(snew)



def f1():
    def inner(a,b):
        print("the sum",a+b)                       #inner and outer functions
        print("The avg",(a+b)/2)
    inner(4,5)
    inner(45,25)
    inner(22,10)
f1()
#Decoraters


def Deco(fuc):
    def inner(name):
        if name=="venky":
            print("hello venky good morning")
        else:
             fuc(name)
    return inner


@Deco                                              #With Decorater
def wish(name):
    print("hey",name,"Good Evening")
#decorater=Deco(wish)                              #with out Decorater
wish("venky")
wish("ram")
wish("venkat")
#decorater("venky")                                #passing values




