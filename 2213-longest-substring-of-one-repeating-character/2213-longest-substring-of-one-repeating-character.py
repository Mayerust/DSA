class SegmentTreeNode:
    def __init__(self, start, end, char=None):
        self.start = start
        self.end = end
        
        self.left_char = char
        self.left_len = 1 if char else 0
        
        self.right_char = char
        self.right_len = 1 if char else 0
        
        self.max_len = 1 if char else 0
        self.is_full = True if char else False
        
        self.left_child = None
        self.right_child = None

class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.s = list(s)
        self.root = self.build_tree(0, self.n - 1)

    def build_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.s[start])
            
        mid = (start + end) // 2
        node = SegmentTreeNode(start, end)
        node.left_child = self.build_tree(start, mid)
        node.right_child = self.build_tree(mid + 1, end)
        
        self.merge(node)
        return node
        
    def merge(self, node):
        left = node.left_child
        right = node.right_child
        
        node.left_char = left.left_char
        node.left_len = left.left_len
        if left.is_full and left.right_char == right.left_char:
            node.left_len += right.left_len
            
        node.right_char = right.right_char
        node.right_len = right.right_len
        if right.is_full and right.left_char == left.right_char:
            node.right_len += left.right_len
            
        node.is_full = left.is_full and right.is_full and left.right_char == right.left_char
        
        node.max_len = max(left.max_len, right.max_len)
        if left.right_char == right.left_char:
            node.max_len = max(node.max_len, left.right_len + right.left_len)
            
    def update(self, index, char):
        self._update_recursive(self.root, index, char)
        
    def _update_recursive(self, node, index, char):
        if node.start == node.end == index:
            node.left_char = node.right_char = char
            return
            
        mid = (node.start + node.end) // 2
        if index <= mid:
            self._update_recursive(node.left_child, index, char)
        else:
            self._update_recursive(node.right_child, index, char)
            
        self.merge(node)
        
    def get_max_len(self):
        return self.root.max_len

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree = SegmentTree(s)
        res = []
        
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            char = queryCharacters[i]
            tree.update(idx, char)
            res.append(tree.get_max_len())
            
        return res