def solution(alp, cop, problems):
    max_alp = max(alp, max(p[0] for p in problems))
    max_cop = max(cop, max(p[1] for p in problems))

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    INF = 100000000000000000000
    dp = [[INF] * (max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0

    for a in range(alp, max_alp+1):
        for c in range(cop, max_cop + 1):
            cur = dp[a][c]

            if cur == INF:
                continue
        
            # 공부
            if a + 1 < max_alp:
                dp[a+1][c] = min(dp[a+1][c], cur+1)
            if c + 1 < max_cop:
                dp[a][c+1] = min(dp[a][c+1], cur+1)

            # 문제풀기
            for req_a, req_c, r_a, r_c, cost in problems:
                if a >= req_a and c >= req_c:
                    na = min(max_alp, a+r_a)
                    nc = min(max_cop, c+r_c)
                    dp[na][nc] = min(dp[na][nc], cur+cost)
    
    return dp[max_alp][max_cop]