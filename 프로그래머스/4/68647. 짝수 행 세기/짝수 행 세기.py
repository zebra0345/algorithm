def solution(a):
    MOD = 10**7 + 19
    R = len(a)
    C = len(a[0])
    
    
    # 조합 미리 계산
    comb = [[0] * (R+1) for _ in range(R+1)]
    for i in range(R+1):
        comb[i][0] = 1
        for j in range(1, i+1):
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD
    
    # 각 열에 대해 1의 총 개수들을 구함
    count = [0] * C
    for r in range(R):
        for c in range(C):
            if a[r][c] == 1:
                count[c] += 1
    
    
    # i 번째 열까지 채웠을 때 1의 개수가 홀수인 행이 j개인 경우의 수
    dp = [[0] * (R + 1) for _ in range(C+1)]
    dp[0][0] = 1
    
    for c in range(1, C+1):
        # 현재 열에 배치해야할 1의 총 개수는 몇개인가
        # 홀수개를 계산해놨으니 여기에서 체크
        K = count[c-1]
        
        for prev_odd in range(R+1):
            if dp[c-1][prev_odd] == 0:
                continue
            
            prev_even = R-prev_odd # 기존 짝수행의 갯수
            
            # x : 기존 홀수행에 배치할 1의 개수(1을 더하면 짝수가 된다)
            # y : 기존 홀수행에 배치할 1의 개수(1을 더하면 홀수가 된다)

            for x in range(K+1):
                y = K- x
                if x <= prev_odd and y <= prev_even:
                    # 새롭게 갱신되는 홀수행의 개수 (기존 홀수 - 짝수로 변한거 + 홀수로 변한거)
                    new_odd = prev_odd - x + y
                    
                    # 경우의 수 계산 (홀수행 중 x 개 선택) * (짝수 행 중 y 개 선택)
                    ways = (comb[prev_odd][x] * comb[prev_even][y]) % MOD
                    
                    dp[c][new_odd] = (dp[c][new_odd] + dp[c-1][prev_odd] * ways) % MOD
                
    
    return dp[C][0]