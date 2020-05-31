import re
str = ""
port={}
f = open("exam2.txt", "r")
all=f.read()
# 

res=(re.findall(r"\] [0-9]*.[0-9]*.[0-9]*.[0-9]*:[0-9]*", all) )# <_sre.SRE_Match object; span=(12, 15), match='cat'>
# print(type(res))

for i in res:
    sp=i.split(':')[0]
    sp=sp.split(' ')[1]
    # print(sp)
    if port.has_key(sp):    
        port[sp]= port[sp]+1
        # print('has')
    else:
        port[sp]=1
res=sorted(port.items(),key=lambda item:item[1])
print(res)
