import sys
read = sys.stdin.readline
 
n,s,r = map(int, read().split())
broke = list(map(int,read().split()))	#카약이 부서진 팀
redun = list(map(int,read().split()))	#여분이 있는 팀
broke, redun = list(set(broke)-set(redun)), list(set(redun)-set(broke))	
#broke, redun = 강풍에 카약이 망가졌지만 여분이 있는 경우
 
ans = 0
for i in broke:	#카약이 망가진 팀 중에
    if i-1 in redun:	#이전 팀에서 여분이 있다면 빌려주기
        redun.remove(i-1)	#여분이 있는 팀 목록에서 이전 팀 삭제
    elif i+1 in redun:	#다음 팀에서 여분이 있다면 빌려주기
        redun.remove(i+1)	#여분이 있는 팀 목록에서 다음 팀 삭제
    else:
        ans += 1	#둘 다 아닌 경우(카약을 못 빌림)
 
print(ans)