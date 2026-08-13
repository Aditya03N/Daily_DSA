nums=[1,2,1,1,4,0,0,0,0,0]
dict={}
for i in range(0,len(nums)):
    if nums[i] not in dict:
        dict[nums[i]]=1

    else:
        dict[nums[i]]+=1    

max_key = max(dict, key=dict.get)   # key whose value is max
print(max_key)   