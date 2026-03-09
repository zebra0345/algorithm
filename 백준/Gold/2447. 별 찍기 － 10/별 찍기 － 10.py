N = int(input())


def draw_start(n):
    if n == 1:
        return ["*"]

    small_stars = draw_start(n // 3)
    result = []
    
    for s in small_stars:
        result.append(s * 3)
    
    for s in small_stars:
        empty = " " * (n // 3)
        result.append(s + empty + s)
    
    for s in small_stars:
        result.append(s * 3)
        
    return result

result = draw_start(N)
for line in result:
    print(line)