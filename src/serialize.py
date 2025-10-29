class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    """Serialize binary tree into string using preorder traversal with '#' for None."""
    def helper(node):
        if node is None:
            return ['#']
        return [str(node.val)] + helper(node.left) + helper(node.right)
    
    return ' '.join(helper(root))

def deserialize(s):
    """Deserialize string back to binary tree."""
    tokens = iter(s.split())

    def helper():
        val = next(tokens)
        if val == '#':
            return None
        # Convert to int if possible
        try:
            val_cast = int(val)
        except ValueError:
            val_cast = val
        node = Node(val_cast)
        node.left = helper()
        node.right = helper()
        return node

    return helper()
