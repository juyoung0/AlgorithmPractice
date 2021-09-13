from collections import defaultdict
from collections import deque
class Node(object):
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, type, data):
        self.root = self._insert(self.root, type, data)
        return self.root is not None

    def _insert(self, node, type, data):
        if node is None:
            node = Node(type, data)
        else:
            if data <= node.data:
                node.left = self.insert(node.left, type, data)
            else:
                node.right = self.insert(node.right, type, data)
        return node

    def find_parent(self, parent):
        return self._find_parent(self.root, parent)

    def _find_parent(self, node, parent):
        parenet_node = None
        if node == None:
            return None
        if parent == node.data:
            return node
        else:
            if node.left:
                parenet_node = self._find_parent(node.left, parent)
                if parenet_node:
                    return parenet_node
            if node.right:
                parenet_node = self._find_parent(node.right, parent)
                if parenet_node:
                    return parenet_node

    def find_sheep(self, type):
        return self._find(self.root, type)

    def _find(self, node, type):
        if node == None:
            return None
        if type == node.type:
            return node
        else:
            if node.left:
                return self._find(node.left, type)
            if node.right:
                return self._find(node.right, type)

def solution(info, edges):
    answer = 0
    bst = BinaryTree()
    nodes = defaultdict(list)
    for e in edges:
        nodes[e[0]].append(e[1])
    total_sheep = len(info) - sum(info)
    keys = sorted(list(nodes.keys()))
    insert_q = deque()
    insert_q.append(0)
    print(nodes)
    while len(insert_q) > 0:
        key = insert_q.popleft()
        if key == 0:
            node = Node(info[key], key)
            bst.root = node
        p_node = bst.find_parent(key)
        nodes[key].sort()
        if p_node:
            if len(nodes[key]) >= 1:
                p_node.left = Node(info[nodes[key][0]], nodes[key][0])
                insert_q.append(nodes[key][0])
            if len(nodes[key]) == 2:
                p_node.right = Node(info[nodes[key][1]], nodes[key][1])
                insert_q.append(nodes[key][1])

    def dfs(node, wolf, sheep, route):
        answer = 0
        if node.type != -1:
            s = abs(node.type - 1)
            w = 1 - s
            sheep += s
            wolf += w
            node.type == -1
            route.append(node.data)

        if sheep == total_sheep:
            return len(route)
        if wolf >= sheep:
            return 0
        else:
            if node.left and node.right:
                answer = max(dfs(node.left, wolf, sheep, route), dfs(node.right, wolf, sheep, route))
            elif node.left:
                answer = dfs(node.left, wolf, sheep, route)
            elif node.right:
                answer = dfs(node.right, wolf, sheep, route)

            answer = max(answer, dfs(bst.find_parent(route[-2]), wolf, sheep, route))
        return answer

    answer = dfs(bst.root, 0, 0, [0])

    return answer

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]), 5)

#print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]), 5)