# this file defines a data structure called Trie that supports CRUD operations

class TrieNode:
    def __init__(self):
        self.children = {}
        self.parent = None
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            prev = cur
            cur = cur.children[c]
            cur.parent = prev
        cur.isWord = True

    def deleteWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        cur.isWord = False  #the word is no longer in the trie
        #if it's not a leaf node, nothing to delete
        if len(cur.children)>0:
            return True
        while not cur.isWord:
            child = cur
            cur = cur.parent
            cur.children.remove(child)  #remove the current trie node
        return True

    def searchWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    def updateWord(self, old_word, new_word):
        result = self.deleteWord(old_word)
        if not result:
            return False
        self.addWord(new_word)
        return True
