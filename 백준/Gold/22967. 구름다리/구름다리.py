import sys

# 1. 건물 개수 N 입력
line = sys.stdin.readline().strip()
if not line:
    exit()
n = int(line)

# 2. 인접 행렬 및 연결 상태 초기화
# 자기 자신과의 연결은 1로 표시
edges = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    edges[i][i] = 1

cnt = 0  # 1번 노드와 연결된 기존 다리 개수
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    edges[u][v] = 1
    edges[v][u] = 1
    
    # 1번 건물과 연결된 경우 카운트
    if u == 1 or v == 1:
        cnt += 1

# 3. 로직 처리 (C++ 코드와 동일)

# n이 4 이하일 때: 완전 그래프를 만들어 지름을 1로 시도
if n <= 4:
    to_add = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if edges[i][j] == 0:
                to_add.append((i, j))
    
    print(len(to_add))
    print(1)
    for u, v in to_add:
        print(f"{u} {v}")

# n이 4 초과일 때: 1번 건물을 중심으로 스타 그래프를 만들어 지름을 2로 고정
else:
    # 1번과 연결되지 않은 모든 노드를 찾아 1번과 연결
    new_edges = []
    for i in range(2, n + 1):
        if edges[1][i] == 0:
            new_edges.append((1, i))
            
    print(len(new_edges))
    print(2)
    for u, v in new_edges:
        print(f"{u} {v}")