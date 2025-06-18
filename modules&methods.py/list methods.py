enames=["rg","sg","pg","rg"]
print(enames)
print(enames[1])
print(enames.index("pg"))
enames.remove("sg")
print(enames)



# update
enames.append("tg")
print(enames)

enames.insert(2,"vk")
print(enames)

print(enames.index("pg"))

print(enames.count("rg"))
print(enames.count("pg"))
enames.insert(4,"abd")
print(enames)
enames.reverse()
print(enames)
enames.sort()
print(enames)
enames.sort(reverse=True)
print(enames)
enames.pop()
print(enames)
