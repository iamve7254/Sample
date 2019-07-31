class TooYoungException(Exception):
    def __init__(self,args):
        self.msg=args

class TooOldException(Exception):
    def __init__(self,args):
        self.msg=args

a=int(input("Enter yours age"))

if a<18:
    raise TooYoungException("yours age age is below 18 so please wait you will get good matchs")
elif a>60:
    raise TooOldException("you are already crosed marrage age so we cant find yours age group matchs")
else:
    print("thanq for regestering you will reseve matches details through mail")



