import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def builder(inorder:list, postorder:list):
    result = []
    def build(in_left, in_right, post_left, post_right):
        # 범위 초과의 경우
        if in_left > in_right or post_left > post_right:
            return []
        
        # 포스트 오더 순회의 마지막 값은 항상 루트
        root = postorder[post_right]

        # 루트노드의 값을 인오더에서 찾아 왼쪽 / 오른쪽 서브트리 분리
        result.append(root)
        root_idx = inorder_index[root]

        # 왼쪽 서브트리 노드갯수
        left_size = root_idx - in_left


        # 루트 -> 왼쪽 -> 오른쪽 서브트리(전위순회)
        build(in_left, root_idx - 1, post_left, post_left + left_size - 1)
        build(root_idx + 1, in_right, post_left + left_size, post_right - 1)
    # 인덱스값의 딕셔너리 생성
    inorder_index = {value: idx for idx, value in enumerate(inorder)}
    build(0, len(inorder) - 1, 0, len(postorder) - 1)
    return result

n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

preorder = builder(inorder, postorder)
sys.stdout.write(' '.join(map(str, preorder)) + '\n')