# TreeAlgorithm 전위, 중위, 후위 순회
# 전위: root => left => right
# 중위: left => root => right
# 후위: left => right => root

N = int(input())
tree_nodes = {}

for i in range(1, N+1):
    root, left, right = list(map(str, input().split()))
    tree_nodes[root] = [left, right]

def preorder(root):
    if root != ".":
        print(root, end='')
        preorder(tree_nodes[root][0])
        preorder(tree_nodes[root][1])

def inorder(root):
    if root != ".":
        inorder(tree_nodes[root][0])
        print(root, end='')
        inorder(tree_nodes[root][1])

def postorder(root):
    if root != ".":
        postorder(tree_nodes[root][0])
        postorder(tree_nodes[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()