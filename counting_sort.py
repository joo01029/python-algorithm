data = [1,2,1,3,4,5,2,3,1,3,2,1,1,5,4,3,3,4,2,1,5]
a = [0,0,0,0,0]
dataa = []
for i in data:
    a[i-1]+=1

for i in range(len(a)):
    for j in range(a[i]):
        dataa.append(i+1)

print(dataa)