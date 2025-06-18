# import json
# fp=open('cust.json','r')
# customers=json.load(fp)
# print(type (customers))
# print(customers)

# for cust in customers:
#     print("customers list",cust)

# fp.close()












# import json
# fp=open('cust.json','r')
# customers=json.load(fp)
# print(type(customers))
# print(customers)

# for cust in customers:
#     print("customers list")

# fp.close()













import json
fp=open('cust.json','r')
customers=json.load(fp)
print(type(customers))
print(customers)

for cust in customers:
    print("list of customers",cust)

fp.close()
