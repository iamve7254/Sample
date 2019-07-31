import re
count=0
#match=re.finditer('[A-Z,0-9]','asAjh@jmZ5KcB')
#match=re.finditer('\d','asAj h@jmZ5KcB')     #\s,\S,\d,\D,\w,\W,.
match=re.finditer('a*','abaabaaabbbB')          #a-->exactly one a,a+-->atleast one a,a*,a?,a{n}-->exactly n no of a's
#match=re.finditer('^a','abaabaaabbbB')   # ^a starts a or not,a$ends a or not
for mach in match:
    count=count+1
    print(mach.start(),'...',mach.group())
print("no of matched:",count)


#
# [abc]----->either a or b or c
# [^abc]---->Except a or b or c
# [a-z]-----> any lower care alphabet symbol
# [A-Z]-----> any upper care alphabet symbol
# [a-z,A-Z]----->any lower and upper
# [a-z,A-Z.0-9]---->any alpha numeric
# [^a-z]--->except lower a-z