import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5 + 10)

def solve(left, right, heights):
    if left == right:
        return heights[left]
    
    mid = (left + right) // 2
    
    left_area = solve(left, mid, heights)
    right_area = solve(mid + 1, right, heights)
    
    lo = mid
    hi = mid + 1
    min_h = min(heights[lo], heights[hi])
    max_area = min_h * 2
    
    # 양쪽으로 확장
    while left < lo or hi < right:
        if hi < right and (lo == left or heights[lo - 1] < heights[hi + 1]):
            hi += 1
            min_h = min(min_h, heights[hi])
        else:
            lo -= 1
            min_h = min(min_h, heights[lo])
            
        max_area = max(max_area, min_h * (hi - lo + 1))
        
    return max(left_area, right_area, max_area)

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    
    n = data[0]
    heights = data[1:]
    
    print(solve(0, n - 1, heights))