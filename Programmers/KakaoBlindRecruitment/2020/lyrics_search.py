# trie 구조
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.children = {}
        self.count = 0

    def get_key(self):
        return self.key

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)

            current_node = current_node.children[char]

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix, wildcard):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0

        current_node = [current_node]
        next_node = []

        cnt = 0
        while True:
            for node in current_node:
                if node.data and cnt == wildcard:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0 and cnt < wildcard:
                current_node = next_node
                next_node = []
            else:
                break
            cnt += 1

        return len(words)


def solution(words, queries):
    answer = []
    front_trie = Trie()
    back_trie = Trie()

    for word in words:
        front_trie.insert(word)
        back_trie.insert(word[::-1])

    for query in queries:
        if query[-1] == '?':
            w = query.count('?')
            p = query[:len(query) - w]
            print(query, w, p)
            answer.append(front_trie.starts_with(p, w))
        else:
            w = query.count('?')
            p = query[w:][::-1]
            print(query, w, p)
            answer.append(back_trie.starts_with(p, w))
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]), [3, 2, 4, 1, 0])
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao", "kokao", "fakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "???ao", "?akao"]), [3, 2, 4, 1, 0, 3, 2])