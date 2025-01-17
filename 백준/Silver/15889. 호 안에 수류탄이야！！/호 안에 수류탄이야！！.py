import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
if n == 1:
    print("권병장님, 중대장님이 찾으십니다")
else:
    temp = list(map(int,input().split()))
    st = [data[0] + temp[0]]
    for i in range(n-1):
        if data[i] <= st[-1]:
            if data[i] + temp[i] >= st[-1]:
                st.pop()
                st.append(data[i] + temp[i])
        else:
            break    
    if data[n-1] <= st[-1]:
        print("권병장님, 중대장님이 찾으십니다")
    else:
        print("엄마 나 전역 늦어질 것 같아")