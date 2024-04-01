import sys
read = sys.stdin.readline

N, M, R = map(int, read().rstrip().split(' '))
ARR = [read().rstrip().split(' ') for _ in range(N)]
R_LIST = list(map(int, read().rstrip().split(' ')))

# 상하 반전
def topAndDown(arr):
  newArr = []
  for r in arr[::-1]:
    newArr.append(r)
  
  return newArr

# 좌우 반전
def leftAndRight(arr):
  newArr = []
  for r in arr:
    newArr.append(r[::-1])
  
  return newArr

# 오른쪽 90도 회전
def degRight90(arr):
  newArr = []
  for c in range(M):
    newArr.append([arr[r][c] for r in range(N-1, -1, -1)])
  
  return [N, M, newArr]

# 왼쪽 90도 회전
def degLeft90(arr):
  newArr = []
  for c in range(M-1, -1, -1):
    newArr.append([arr[r][c] for r in range(N)])
  
  return [N, M, newArr]

# 5번 연산
def solvedN5(arr):
  newArr = []
  n, m = N//2, M//2
  arr1 = [r[0:m] for r in arr[0:n]]
  arr2 = [r[m:] for r in arr[0:n]]
  arr3 = [r[0:m] for r in arr[n:]]
  arr4 = [r[m:] for r in arr[n:]]
  
  newArr.extend([*arr3[i], *arr1[i]] for i in range(n))
  newArr.extend([*arr4[i], *arr2[i]] for i in range(n))

  return newArr

# 6번 연산
def solvedN6(arr):
  newArr = []
  n, m = N//2, M//2
  arr1 = [r[0:m] for r in arr[0:n]]
  arr2 = [r[m:] for r in arr[0:n]]
  arr3 = [r[0:m] for r in arr[n:]]
  arr4 = [r[m:] for r in arr[n:]]
  
  newArr.extend([*arr2[i], *arr4[i]] for i in range(n))
  newArr.extend([*arr1[i], *arr3[i]] for i in range(n))

  return newArr

arr = ARR.copy()
for i in R_LIST:
  if i == 1:
    arr = topAndDown(arr)
  if i == 2:
    arr = leftAndRight(arr)
  if i == 3:
    M, N, arr = degRight90(arr)
  if i == 4:
    M, N, arr = degLeft90(arr)
  if i == 5:
    arr = solvedN5(arr)
  if i == 6:
    arr = solvedN6(arr)

print("\n".join(map(lambda x: " ".join(x), arr)))
