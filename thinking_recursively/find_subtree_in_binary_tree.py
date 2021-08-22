class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def in_order(tree, ll):
    if tree is None:
        return
    
    in_order(tree.left, ll)
    ll.append(tree.data)
    in_order(tree.right, ll)


def pre_order(tree, ll):
    if tree is None:
        return
    
    ll.append(tree.data)
    pre_order(tree.left, ll)
    pre_order(tree.right, ll)


def is_subtree(tree, subtree):

    if subtree is None:
        return True
    
    if tree is None:
        return False

    first = []
    second = []

    in_order(tree, first)
    in_order(subtree, second)

    first_str = first.__str__().replace("[","").replace("]","")
    second_str = second.__str__().replace("[","").replace("]","")

    if first_str.find(second_str) == -1:
        return False
    
    first = []
    second = []

    pre_order(tree, first)
    pre_order(subtree, second)

    third_str = first.__str__().replace("[","").replace("]","")
    fourth_str = second.__str__().replace("[","").replace("]","")

    if third_str.find(fourth_str) == -1:
        return False
    
    return True
    



first_root = Node(1)
first_root.left = Node(2)
first_root.right = Node(3)
first_root.left.left = Node(4)
first_root.left.right = Node(5)
first_root.right.left = Node(6)
first_root.right.right = Node(7)


second_root = Node(3)
second_root.left = Node(6)
second_root.right = Node(7)


print(is_subtree(first_root, second_root))