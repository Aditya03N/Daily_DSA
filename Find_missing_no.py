arr=[4,5,7,6,1,2,3]
n=int(len(arr)+1)
sum = 0
real_sum=(n*(n+1))/2

for i in arr:
    sum+=i
no=real_sum-sum
print(no)