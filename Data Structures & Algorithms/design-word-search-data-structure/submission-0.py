class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(i: int, node: TrieNode):
            cur = node

            for j in range(i, len(word)):
                char = word[j]
                if char == ".":
                    for child in cur.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.word
        return dfs(0, self.root)
