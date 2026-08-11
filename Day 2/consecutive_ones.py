arr=[1,1,1,1,1,0,1,1,1,0,1,1,1,1]
count=0
count1=0

for i in arr:
    if i==1:
        count+=1
        count1=max(count1,count)

    else:
        count=0

print(count1)    