A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())
answer = 0

for _ in range(3):
    chicken = min(A, X)
    answer += chicken
    A -= chicken
    X -= chicken

    pizza = min(B, Y)
    answer += pizza
    B -= pizza
    Y -= pizza

    burger = min(C, Z)
    answer += burger
    C -= burger
    Z -= burger
    
    Y, Z, X = X // 3, Y // 3, Z // 3

print(answer)