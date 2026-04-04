import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    lines = []
    idx = 1
    for _ in range(N):
        lines.append((int(data[idx]), int(data[idx+1])))
        idx += 2
        
    lines.sort()
    
    total_length = 0
    cur_start = lines[0][0]
    cur_end = lines[0][1]
    
    for i in range(1, N):
        next_start, next_end = lines[i]
        
        if next_start <= cur_end:
            cur_end = max(cur_end, next_end)
        else:
            total_length += (cur_end - cur_start)
            cur_start = next_start
            cur_end = next_end
            
    total_length += (cur_end - cur_start)
    print(total_length)

solve()