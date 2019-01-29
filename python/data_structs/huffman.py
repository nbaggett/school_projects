from priorityqueue import *
from collections import OrderedDict

class Node:
    
    def __init__(self, freq, char, left, right):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.pri = 1/freq 

def huffman(phrase):
    d = OrderedDict()
    dup = []
    for c in phrase:
        if c not in dup:
            dup.append(c)
            d[c] = phrase.count(c)
    
    q = PriorityQueue()
    
    for key, value in d.items():
        singlenode = Node(value, key, None, None)
        q.enqueue(singlenode, 1/singlenode.freq - ord(singlenode.char)/100000)
        
    while q.length > 1:
        t1 = q.dequeue()
        t2 = q.dequeue()
        
        freq = int(t1.freq + t2.freq)
        pri = 1/freq
        tree = Node(freq, t1.char + t2.char, t1, t2)
        q.enqueue(tree, tree.pri)

    return q.dequeue()

dic = {}
def inorder(root, search, s):
    if root:
        if root.char == search:
            dic[search] = s
            return True
        if root.left:
            inorder(root.left, search, s+'0')
        if root.right:
            inorder(root.right, search, s+'1')

def get_huffman_code(ch, tree):
    k = inorder(tree, ch, '')
    return dic[ch]


def main():
    #s = 'aaaaggccttt'
    #s = 'testing this string'
    #s = 'StringTeessttt'
    s = 'asdf;k;lkjasdfk'
    root = huffman(s)
    print()
    codes = {}
    for ch in s:
        codes[ch] = get_huffman_code(ch, root)
    print(codes)
    
if __name__ == '__main__':
    main()