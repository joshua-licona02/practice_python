from collections import deque
class TreeNode:
    def __init__(self, key):
        self.key=key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)
    
    def _insert_recursively(self, root, key):
        if root is None:
            return TreeNode(key)
        elif key< root.key:
            root.left = self._insert_recursively(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursively(root.right, key)
        return root
    
    def dfs_inorder(self):
        self._dfs_inorder_recursively(self.root)
    
    def _dfs_inorder_recursively(self, root):
        if root:
            self._dfs_inorder_recursively(root.left)
            print(root.key, end=" ")
            self._dfs_inorder_recursively(root.right)

    def dfs_preorder(self):
        self._dfs_preorder_recursively(self.root)

    def _dfs_preorder_recursively(self, root):
        if root:
            print(root.key, end=" ")
            self._dfs_preorder_recursively(root.left)
            self._dfs_preorder_recursively(root.right)
    
    def dfs_postorder(self):
        self._dfs_postorder_recursively(self.root)
    
    def _dfs_postorder_recursively(self, root):
        if root:
            self._dfs_preorder_recursively(root.left)
            self._dfs_preorder_recursively(root.right)
            print(root.key, end = " ")

    # Print visual
    def print_visual(self): 
        self._print_visual_recursively(self.root, 0)

    def _print_visual_recursively(self, root, depth):
        if root:
            self._print_visual_recursively(root.right, depth + 1)
            print("    " * depth + str(root.key))
            self._print_visual_recursively(root.left, depth + 1)


bst = BinarySearchTree()

bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

bst.print_visual()

print("Inorder: ") 
bst.dfs_inorder()
print("\n")

print("Preoder: ") 
bst.dfs_preorder()
print("\n")

print("Inorder: ") 
bst.dfs_postorder()
print("\n")


