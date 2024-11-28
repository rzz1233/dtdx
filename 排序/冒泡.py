list=[2,3,5,4,9,6]

for i in range(len(list)-1):
    for j in range(0,len(list)-1-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

print(list)