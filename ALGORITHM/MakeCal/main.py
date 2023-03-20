# make a calculator
# + - < * /

# 1. 후위 순회 이용하기
# def postorder_traverse(T):
#     if T is not null:
#         postorder_traverse(T.left)
#         postorder_traverse(T.right)
#         visit(T)

# 2. Stack에 연산 결과 저장하기

class Stack:
    def createStack(self):
        self.stack = []

    def push(self,e):
        self.stack.append(e)

    def pop(self):
        if len(self.stack) == 0:
            print("Error")
        else:
            self.stack.pop(-1)

    def printCal(self):
        print(self.stack)

class Node:
    def createNode(self, data):


