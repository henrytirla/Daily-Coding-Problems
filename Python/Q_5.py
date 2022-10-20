"""This problem was asked by Google.

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

##Definition

Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stroed in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment

#useful resource
https://www.youtube.com/watch?v=Qtf8ieq3zco
https://www.youtube.com/watch?v=u4JAi2JJhI8
"""

