N = int(input())

arr2 = []
arr3 = []

def hanoi(n, start, end):
    if n == 1:
        arr2.append(start)
        arr3.append(end)
    else:
        hanoi(n - 1, start, 6 - start - end)
        arr2.append(start)
        arr3.append(end)
        hanoi(n - 1, 6 - start - end, end)

hanoi(N, 1, 3)

print(len(arr2))
for i in range(len(arr2)):
    print(arr2[i], arr3[i])