class PrefixTree:

    def __init__(self):
        self.words = set()
        self.prefixs = set()        

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word)):
            self.prefixs.add(word[:i+1])

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefixs:
            return True
        return False
        