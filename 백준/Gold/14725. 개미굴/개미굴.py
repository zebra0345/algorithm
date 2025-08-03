import sys
input = sys.stdin.readline

class Ant:
    def __init__(self):
        self.children = dict()
    
    def insert(self, foods):
        node = self
        for food in foods:
            if food not in node.children:
                node.children[food] = Ant()
            node = node.children[food]
    
    def dfs(self, depth=0):
        for key in sorted(self.children):
            print("--" * depth + key)
            self.children[key].dfs(depth + 1)
    

n = int(input())
root = Ant()

for _ in range(n):
    data = input().split()
    k = int(data[0])
    foods = data[1:]
    root.insert(foods)

root.dfs()