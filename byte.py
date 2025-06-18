enames=["Rahul","Sonai","Priyainka"]    #list 
eids=(101,102,103,104)      #tuple
uids={10,11,12,13,14}    #set
emp={
    'eid':101,
    'ename':'Rahul'
}
range_Value=range(100)
ename="Rahul Gandhi"

print('Rahul' in enames)   #True
print('eid' in emp)

#frizenset
list1=[80,40,81,14]
b=bytes(list1)
print(81 in b)
print(82 in b )

ba=bytearray([80,40,81,14])
print(type(ba))
print(81 in ba)
print(82 not in ba)
ba[3]=18

