import sys
rl = sys.stdin.readline

N = int(rl().rstrip())
FILES = list(map(lambda _: rl().rstrip(), range(N)))

fileDict = dict()
for file in FILES:
  ext = file.split('.')[1]
  if ext in fileDict:
    fileDict[ext] += 1
  else:
    fileDict[ext] = 1
  
print("\n".join(list(map(lambda ext: f'{ext} {fileDict[ext]}',sorted(fileDict)))))
