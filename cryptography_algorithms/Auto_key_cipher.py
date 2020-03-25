pt = input("enter the plain text: ")
key =int(input("enter the key: "))

pt = list(pt)
temp = list()
t = list()
ct = ""


for i in range(len(pt)):
	t.append(ord(pt[i]) - 97)

temp.append(t[0] + key)

for i in range(len(pt)):
	temp.append(t[i])

for i in range(len(pt)):
	ct = ct + chr((temp[i] + t[i])%26 + 97)

print(ct)		

