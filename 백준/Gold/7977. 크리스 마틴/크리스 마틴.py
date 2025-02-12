import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    dna = sys.stdin.readline().rstrip()
    atgc = [dna.count('A'), dna.count('T'), dna.count('G'), dna.count('C')]
    min_atgc = min(atgc)
    print(min_atgc)
    if atgc[0] == min_atgc:
        print('A'*N)
    elif atgc[1] == min_atgc:
        print('T'*N)
    elif atgc[2] == min_atgc:
        print('G'*N)
    else:
        print('C'*N)