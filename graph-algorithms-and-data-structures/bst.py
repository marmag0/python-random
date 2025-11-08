#! /usr/bin/env python3

class BST:
    #constructor for the Binary Search Tree
    def __init__(self, value, left=None, right=None):
        self.val = value    #parent node
        self.left = None    #left child (<value)
        self.right = None   #right child (>value)

    #inserting a value into the Binary Search Tree
    def insert_to_BST(self, value):
        if value >= self.val:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert_to_BST(value)
        else:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert_to_BST(value)

    #finding a value in the Binary Search Tree
    def find_val(self, value, steps=None):
        if steps is None:
            steps = ['root']
        if self.val == value:
            return [True, value, steps]
        elif value < self.val and self.left is not None:
            steps.append("<-")
            return self.left.find_val(value, steps)
        elif value > self.val and self.right is not None:
            steps.append("->")
            return self.right.find_val(value, steps)
        return [False, value, steps]

    #deleting a value from the Binary Search Tree
    def delete_val(self, value):
        if value < self.val:
            if self.left:
                self.left = self.left.delete_val(value)
        elif value > self.val:
            if self.right:
                self.right = self.right.delete_val(value)
        else:
            #node with no children
            if self.left is None and self.right is None:
                return None
            #node with only one child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            #node with two children:
            #dind the in-order successor (smallest in the right subtree)
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            self.val = min_larger_node.val  #replace value
            self.right = self.right.delete_val(min_larger_node.val)  #delete successor
        return self
    
    #value remover safeguard
    def safe_delete_val(self, value):
        if (self.find_val(value))[0]:
            print(f"\nBegining removal of value #{value}#")
            self.delete_val(value)
            print("Removal complited successfuly")
        else:
            print(f"\nValue #{value}# not found!")
            print("Removal ERROR!")
    
    #in-order traversal of the Binary Search Tree -> max left, then to the parent, then max right
    #can be used to sort in ascending order
    def in_order_traversal(self):
        if self.left is not None:
            self.left.in_order_traversal()
        print(self.val, end=' ')
        if self.right is not None:
            self.right.in_order_traversal()

    #pre-order traversal of the Binary Search Tree -> parent, then max left, then max right
    def pre_order_traversal(self):
        print(self.val, end=' ')
        if self.left is not None:
            self.left.pre_order_traversal()
        if self.right is not None:
            self.right.pre_order_traversal()

    #post-order traversal of the Binary Search Tree -> max right, then to the parten, then max left
    #can be used to sort in descending order
    def post_order_traversal(self):
        if self.right is not None:
            self.right.post_order_traversal()
        print(self.val, end=' ')
        if self.left is not None:
            self.left.post_order_traversal()
    

def main():
    array = [4, 3, 5, 8, 9, 2]
    
    bst = BST(array[0])
    for i in range(1, len(array)):
        bst.insert_to_BST(array[i])

    search_outcome = bst.find_val(9)
    if search_outcome[0]:
        print(f"Value #{search_outcome[1]}# found. Steps taken: {search_outcome[2]}")
    else:
        print(f"Value #{search_outcome[1]}# not found. Steps taken: {search_outcome[2]}")
    
    print("In-order traversal of the BST: ", end="")
    bst.in_order_traversal()
    print()

    print("Pre-order traversal of the BST: ", end="")
    bst.pre_order_traversal()
    print()

    print("Post-order traversal of the BST: ", end="")
    bst.post_order_traversal()
    print()

    bst.safe_delete_val(3)
    bst.safe_delete_val(3)
    print("In-order traversal of the BST: ", end="")
    bst.in_order_traversal()
    print()
    print()
    
    return 0

if __name__ == "__main__":
    main()
