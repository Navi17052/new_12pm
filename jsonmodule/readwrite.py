import json
fp1=open('emp.json','r')
fp2=open('user.json','w')

users=json.load(fp1)
print(type(users))

json.dump(users,fp2)
print("new file created!")
fp2.close()
fp1.close()












