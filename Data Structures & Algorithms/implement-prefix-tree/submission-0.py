class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

        

    def insert(self, word: str) -> None:
        parent = self.root
        for i in word:
            if i not in parent.children:
                parent.children[i] = TrieNode()
            parent = parent.children[i]
        parent.end_word = True


    def search(self, word: str) -> bool:
        parent = self.root
        for i in word:
            if i in parent.children:
                parent = parent.children[i]
            else:
                return False
        return parent.end_word
        

    def startsWith(self, prefix: str) -> bool:
        parent = self.root
        for i in prefix:
            if i in parent.children:
                parent = parent.children[i]
            else: 
                return False
        return True
        
        