import sys
input = sys.stdin.readline

input = sys.stdin.readline

N, Q = map(int, input().split())

S = [set(input().split()[1:]) for _ in range(N)]

for _ in range(Q):
        tmp = input().split()
        if tmp[0] == '1':
            a, b = int(tmp[1]) - 1, int(tmp[2]) - 1
            if len(S[a]) < len(S[b]):
                S[a], S[b] = S[b], S[a]
            S[a].update(S[b])
            S[b].clear()
        else:
            a = int(tmp[1]) - 1
            print(len(S[a]))