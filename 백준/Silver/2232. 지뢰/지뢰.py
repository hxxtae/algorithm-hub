import sys
read = sys.stdin.readline
N = int(read().strip())

nums = [0]
for _ in range(N):
    nums.append(int(read().strip()))
nums.append(0)

rst = []
for i in range(1, N+1):
    if nums[i-1] <= nums[i] >= nums[i+1]:
        rst.append(i)

print('\n'.join(map(str, rst)))