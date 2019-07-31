import re


count=0
#pattern=re.compile('ba')
matchs=re.finditer('ab','abaababa')
for match in matchs:
    count = count + 1
    #print("i am matching available index:",match.start())
    print("start:{},end:{},group:{}".format(match.start(),match.end(),match.group()))
print("no of matchings:",count)