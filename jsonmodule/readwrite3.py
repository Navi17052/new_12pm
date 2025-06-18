fp=open('readjson2.py','r')
data=fp.read()

fp1=open('readjson1','w')
fp1.write(data)

print("created")

fp1.close()
fp.close()