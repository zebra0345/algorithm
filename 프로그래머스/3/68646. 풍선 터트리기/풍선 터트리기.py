def solution(a):
    if len(a) <= 2:
        return len(a)
    
    answer = 0
    n = len(a)
    
    left_min = [0] * n
    left_min[0] = a[0]
    
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
    
    right_min = [0] * n
    right_min[-1] = a[-1]
    
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i])
    
    for i in range(n):
        if i == 0 or i == n-1:
            answer += 1
            continue
        
        if a[i] > left_min[i-1] and a[i] > right_min[i+1]:
            continue
        
        answer += 1
    
    return answer