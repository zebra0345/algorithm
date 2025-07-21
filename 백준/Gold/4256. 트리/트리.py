T = int(input())



def builder(pre, mid):
    if not pre or not mid:
        return []
    
    root = pre[0]
    root_index = mid.index(root)

    left_mid = mid[:root_index]
    right_mid = mid[root_index+1:]

    left_pre = pre[1:1 + len(left_mid)]
    right_pre = pre[1 + len(left_mid):]

    left_post = builder(left_pre, left_mid)
    right_post = builder(right_pre, right_mid)

    return left_post + right_post + [root]

for _ in range(T):
    N = int(input())
    pre = list(map(int, input().split()))
    mid = list(map(int, input().split()))

    post = builder(pre, mid)
    print(*post)
