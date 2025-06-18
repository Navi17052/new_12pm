fp=open('decorator1.py','r')
data=fp.read()

fp1=open('dec.py','w')
fp1.write(data)


print("created")

fp.close()
fp1.close()