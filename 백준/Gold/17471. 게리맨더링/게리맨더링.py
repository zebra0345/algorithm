from itertools import combinations
from collections import deque

N = int(input())
population_list = list(map(int, input().split()))

node_map = [[] for _ in range(N+1)]
for i in range(1, N+1):
    info = input().split()
    node_len, around = int(info[0]), list(map(int, info[1:]))
    
    node_map[i].extend(around)

def is_connected(nodes, node_map):
    if not nodes:
        return False
    if len(nodes) == 1:
        return True
    
    start_node = nodes[0]
    queue = deque([start_node])
    visited = {start_node}
    node_set = set(nodes)

    count = 0
    while queue:
        current = queue.popleft()
        count += 1
        for neighbor in node_map[current]:
            if neighbor in node_set and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return count == len(nodes)

def solve():
    if N < 2:
        return -1
        
    min_diff = float('inf')
    total_population = sum(population_list)

    all_districts = list(range(1, N + 1))
    
    for k in range(1, N): 
        for group_a_tuple in combinations(all_districts, k):
            group_a = list(group_a_tuple)
            group_b = list(set(all_districts) - set(group_a))
            
            is_a_connected = is_connected(group_a, node_map)
            is_b_connected = is_connected(group_b, node_map)
            
            if is_a_connected and is_b_connected:
                pop_a = sum(population_list[i - 1] for i in group_a)
                pop_b = total_population - pop_a
                
                diff = abs(pop_a - pop_b)
                min_diff = min(min_diff, diff)
                    
    # 4. 결과 출력
    if min_diff == float('inf'):
        return -1
    else:
        return min_diff

print(solve())