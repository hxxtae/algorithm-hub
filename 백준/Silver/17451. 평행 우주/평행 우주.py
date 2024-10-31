import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int,read().split()))
speed = nums[-1]

for i in range(n-2, -1, -1):
    if nums[i] > speed:
        speed = nums[i] 
    else: 
        if speed%nums[i]: 
            speed = (speed//nums[i]+1) *nums[i] 
print(speed)