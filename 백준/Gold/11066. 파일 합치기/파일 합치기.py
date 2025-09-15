T = int(input().strip())
INF = 10**18

for _ in range(T):
    K = int(input().strip())
    pages = [0] + list(map(int, input().split()))  # 1-index

    # prefix sum
    s = [0] * (K + 1)
    for i in range(1, K + 1):
        s[i] = s[i - 1] + pages[i]

    dp = [[0] * (K + 1) for _ in range(K + 1)]
    opt = [[0] * (K + 1) for _ in range(K + 1)]
    for i in range(1, K + 1):
        opt[i][i] = i  

    for length in range(2, K + 1):
        for i in range(1, K - length + 2):
            j = i + length - 1
            dp[i][j] = INF

            # Knuth: opt[i][j-1] <= opt[i][j] <= opt[i+1][j]
            L = opt[i][j - 1] if opt[i][j - 1] != 0 else i
            R = opt[i + 1][j] if (i + 1 <= j and opt[i + 1][j] != 0) else j - 1

            # 창 범위 보정
            if L < i: L = i
            if R > j - 1: R = j - 1
            if L > R:  
                L, R = i, j - 1

            best = L
            total = s[j] - s[i - 1]
            for k in range(L, R + 1):
                cost = dp[i][k] + dp[k + 1][j] + total
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    best = k
            opt[i][j] = best

    print(dp[1][K])
