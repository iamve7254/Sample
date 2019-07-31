import re
# s=input("enter yourrs matchs")              #first its available or not
# m=re.match(s,'abcdfdg4')
# if m!= None:
#     print("match the available in first")
# else:
#     print("match is not available")
#
#
#
#
#s=input("enter pattern to check")                  #entire data is match or not
# m=re.fullmatch(s,'abgd mafdstahb dbbdd')
# if m!= None:
#     print("match the available in first")
# else:
#     print("match is not available")



#
# s=input("enter pattern to check")                           #enter data chek
# m=re.search(s,'abgd madathala venky7254')
# if m!= None:
#     print("match the available ")
# else:
#     print("match is not available")



# m=re.findall('[a-z]','abgd madathala venky7254')         #finding available vals
# print(m)


# m=re.finditer('\D','aabCdbbds75@')
# for mat in m:
#     print("start index:{},end index:{}".format(mat.start(),mat.end()))



stri=re.sub('\d','x','mobileno:8500981165')               #replaceing
print(stri)


tup=re.subn('\d','x@','mobileno:8500981165')               #tuple values,count liket[0],t[1]
print("the result of string:",tup[0])
print("no of replacements :",tup[1])




spli=re.split('-','10-20-30-40-50-60')
print(spli)


ieg="hey i am testing ignore Case"                      #when you write ignore case it will check lower and Upper case
res=re.search('case$',ieg,re.IGNORECASE)
print(res)





sam=input("Enter Identifier to valid")
m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',sam)
if m!=None:
    print(sam,"is valid yava identifier")
else:
    print(sam,"is not valid yava identifier")


mob=input("enter mobile no")
new=re.fullmatch('[6-9][0-9]{9}',mob) #[6-9]\d{9}
if new!=None:
    print(new,"valid mb no")
else:
    print(new,"not valid mb no")

