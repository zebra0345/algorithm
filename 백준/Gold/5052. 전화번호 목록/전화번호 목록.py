T = int(input())

for _ in range(T):
    N = int(input())
    numbers = []
    for _ in range(N):
        number = input()
        numbers.append(number)

    # 정렬
    numbers.sort()
    for i in range(N-1):
        if numbers[i+1].startswith(numbers[i]):
            print("NO")
            break
    else:
        print("YES")