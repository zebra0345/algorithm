import sys
input = sys.stdin.readline

class Fenwick:
    def __init__(self, n):
        # 관리 값의 개수 설정
        self.n = n
        self.bit = [0] * (n+1)
    
    # 구간 값을 갱신함
    def add(self, i:int, delta:int)->None:
        # i번 위치에 delta를 더함,
        # i = (값+1)
        # delta = 1 (해당 값이 트리에 삽입되었음을 명시)
        n = self.n
        bit = self.bit
        while i <= n:
            bit[i] += delta
            i += i & -i

    # 구간의 합을 구함
    def sum(self, i):
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i] #구간 값 누적
            i -= i & -i
        return s
    
    def kth(self, k):
        # 정렬된 상태에서 k번재 원소의 값 찾기
        idx = 0
        bit = self.bit
        step = 1 << (self.n.bit_length())

        while step:
            nxt = idx + step
            # nxt 까지의 누적합이 k 보가 작으면
            if nxt <= self.n and self.bit[nxt] < k:
                k -= bit[nxt]
                idx = nxt
            step >>= 1
        
        return idx + 1
    

N = int(input().strip())
p = [int(input().strip()) for _ in range(N)]

depth = [0] * N

fw = Fenwick(N)

root = p[0]
depth[root] = 1
fw.add(root+1, 1)
total_node = 1
ans = 1

for x in p[1:]:
    idx = x+1

    # x보다 작은값 계산
    cnt_less = fw.sum(idx-1)
    pred_depth = 0

    # x보다 정렬된 값이 리스트에서 몇개니?
    # x보다 작은 값들은 S[1] ~ S[cnt_less]까지 딱 cnt_less개 존재
    # 가장 큰 값은 마지막원소
    # 팬윅의 kth는 k번쨰 원소의 값 위치
    # 근데 팬윅트리는 +1 해서 우리가 쓸때는 -1
    if cnt_less > 0:
        # 정렬된 상태에서 cnt_less 번째 값
        # x 보다 작은 값 중 가장 큰 값
        pred_val = fw.kth(cnt_less) - 1
        pred_depth = depth[pred_val]
    
    # 오른쪾이웃
    # 작은게 몇개
    cnt_le = fw.sum(idx)

    succ_depth = 0
    if cnt_le < total_node:
        succ_val = fw.kth(cnt_le+1)-1
        succ_depth = depth[succ_val]
    
    # 깊이 계산
    # 새 노드는 왼쪽 오른쪽 이웃 중 더 깊은 쪽의 자식으로
    depth[x] = max(pred_depth, succ_depth) + 1
    ans += depth[x]

    fw.add(idx, 1)
    total_node += 1
print(ans)
