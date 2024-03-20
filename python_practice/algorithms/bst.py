class TreeNode:
    def __init__(self, key):
        self.key = key
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
        elif key < root.key:
            root.left = self._insert_recursively(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursively(root.right, key)
        return root
    
    def search(self, key):
        return self._search_recursively(self.root, key)
    
    def _search_recursively(self, root, key):
        if root is None or root.key == key:
            return root
        elif key < root.key:
            return self._search_recursively(root.left, key)
        return self._search_recursively(root.right, key)
    
    def inorder_traversal(self):
        self._inorder_traversal_recursively(self.root)
    
    def _inorder_traversal_recursively(self, root):
        if root:
            self._inorder_traversal_recursively(root.left)
            print(root.key, end=" ")
            self._inorder_traversal_recursively(root.right)

    # visual representation
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

print("Inorder Traversal")
bst.inorder_traversal()
print("\n")

print("Search for 70: ", bst.search(70))
print("Search for 10: ", bst.search(10))


