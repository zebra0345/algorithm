N = int(input())

num_arr = list(map(int, input().split()))

max_dp = num_arr[:]
min_dp = num_arr[:]

for _ in range(N-1):
    a, b, c = map(int, input().split())

    prev_max = max_dp[:]
    prev_min = min_dp[:]

    max_dp[0] = a + max(prev_max[0], prev_max[1])
    max_dp[1] = b + max(prev_max[0], prev_max[1], prev_max[2])
    max_dp[2] = c + max(prev_max[1], prev_max[2])

    min_dp[0] = a + min(prev_min[0], prev_min[1])
    min_dp[1] = b + min(prev_min[0], prev_min[1], prev_min[2])
    min_dp[2] = c + min(prev_min[1], prev_min[2])

print(max(max_dp), min(min_dp))