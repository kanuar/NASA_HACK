import json
f=open('database\\data.json','r')
data=json.load(f)
ip=[]
for i in data:
    if data[i]==[]:
        ip.append(i)
for i in ip:
    del data[i]

f.close()
f2=open('ff.json','w')
json.dump(data,f2)
f2.close()