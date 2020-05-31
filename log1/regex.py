import re
str = ""
port={}
f = open("exam1.txt", "r")
all=f.read()


res=(re.findall(r"-> [0-9.]*:[0-9]*", all) )
# print(type(res))
for i in res:
    # print(i.split(':')[1])
    if port.has_key(i.split(':')[1]):    
        port[i.split(':')[1]]= port[i.split(':')[1]]+1
        # print('has')
    else:
        port[i.split(':')[1]]=1
res=sorted(port.items(),key=lambda item:item[1])
print(res)

# sha(445143323   )

# 0e2c3e4dd79f9a26e591728c8af4e8347403127a