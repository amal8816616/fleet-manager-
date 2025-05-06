class AVLNode:
    """
    Node for AVL Tree storing User objects by a key (e.g., ride count or rating).
    """
    def __init__(self, user, key):
        self.user = user
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class UserAVLTree:
    """
    AVL Tree to store and sort users by a specified key (ride count or rating).

    Example:
        tree = UserAVLTree()
        tree.insert(User("u001", "Ali", "driver"), 50)
        sorted_users = tree.inorder()  # list of users sorted by ride count
    """

    def __init__(self):
        self.root = None

    def insert(self, user, key):
        self.root = self._insert(self.root, user, key)

    def _insert(self, node, user, key):
        if not node:
            return AVLNode(user, key)

        if key < node.key:
            node.left = self._insert(node.left, user, key)
        else:
            node.right = self._insert(node.right, user, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Rotations
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def inorder(self):
        """
        Returns list of users in ascending order based on the sorting key.
        """
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.user)
            self._inorder(node.right, result)

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
