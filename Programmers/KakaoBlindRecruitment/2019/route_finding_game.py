# 210906: 35분 소요

from collections import deque

class Node(object):
    def __init__(self,x, y, key):
        self.x = x
        self.y = y
        self.key = key
        self.left = None
        self.right = None

    def get_loc(self):
        return [self.x, self.y]

class Tree:
    def __init__(self):
        self.head = None

    def insert(self, x, y, key):
        current_node = self.head
        if not current_node:
            self.head = Node(x, y, key)
            return
        # left child
        while True:
            if x < current_node.x:
                if not current_node.left:
                    current_node.left = Node(x, y, key)
                    break
                else:
                    current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = Node(x, y, key)
                    break
                else:
                    current_node = current_node.right

    def preorder(self):
        order = []
        stack = deque()
        stack.append(self.head)

        while stack:
            current_node = stack.pop()
            order.append(current_node.key)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

        return order

    def postorder(self):
        order = []
        stack = deque()
        stack.append(self.head)

        while stack:
            current_node = stack.pop()
            order.append(current_node.key)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)

        return order[::-1]

def solution(nodeinfo):
    nodeinfo = [[n[0], n[1], i + 1] for i, n in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: x[0])
    nodeinfo.sort(reverse=True, key=lambda x: x[1])
    tree = Tree()
    print(nodeinfo)
    for i, node in enumerate(nodeinfo):
        tree.insert(node[0], node[1], node[2])
    answer = []
    answer.append(tree.preorder())
    answer.append(tree.postorder())
    return answer

print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]), [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]])