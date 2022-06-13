# trie 구조
class Node(object):
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.terminal = False
        self.children = {}

    def get_key(self):
        return self.key


class Trie:
    def __init__(self):
        self.head = Node(None)
        self.count = 0

    def insert(self, string):
        current_node = self.head
        self.count += 1

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            current_node.count += 1

        current_node.terminal = True

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        return current_node.terminal

    def starts_with(self, prefix, wildcard):
        current_node = self.head

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0

        return current_node.count


def solution(words, queries):
    answer = []
    front_trie = {}
    back_trie = {}

    # 글자 길이 수에 따라 trie을 각각 만들어 준다
    # ???갯수에 따라 탐색을 계속 할 필요 없도록 하기 위함이다
    for word in words:
        if len(word) not in front_trie:
            front_trie[len(word)] = Trie()
            back_trie[len(word)] = Trie()

        front_trie[len(word)].insert(word)
        back_trie[len(word)].insert(word[::-1])

    for query in queries:
        if len(query) not in front_trie:
            answer.append(0)
            continue

        # 전부 물음표인 경우
        if len(query) == query.count('?'):
            answer.append(front_trie[len(query)].count)
            continue

        if query[-1] == '?':
            w = query.count('?')
            p = query[:len(query) - w]
            answer.append(front_trie[len(query)].starts_with(p, w))
        else:
            w = query.count('?')
            p = query[w:][::-1]
            answer.append(back_trie[len(query)].starts_with(p, w))
    return answer