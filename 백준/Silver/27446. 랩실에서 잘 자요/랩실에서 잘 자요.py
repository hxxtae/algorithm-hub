import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pages = sorted(list(map(int, input().split())))
no_page = []
for page in range(1,n+1):
  if page not in pages:
    no_page.append(page)

last = 0
ink = 0
for i in no_page:
  if last:
    ink += min(7,(i-last)*2)
  else:
    ink += 7
  last = i
print(ink)