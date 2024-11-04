import sys
input = sys.stdin.readline

while True:
    try:
        s, t = map(str, input().split())
 
        flag = 0
        idx = 0
        for i in range(len(t)):
            if s[idx] == t[i]:
                idx += 1
 
            # 만약 s를 모두 체크했다면
            if(idx == len(s)):
                flag = 1
                break
 
        if flag:
            print("Yes")
        else:
            print("No")
 
    except:
        break