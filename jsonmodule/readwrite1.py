import json
fp1=open('std.json','r')
fp2=open('stds.json','w')

l1=json.load(fp1)
print(type(l1))


json.dump(l1,fp2)
print("list of students!")

fp1.close()
fp2.close()