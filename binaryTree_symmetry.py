"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric.
But the following is not:

    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem


Solution:
2 trees T1 and T2 are symmetric if
1) value of T1’s root is same as T2’s root
2) T1’s left and T2’s right are symmetric.
3) T2’s left and T1’s right are symmetric.

"""
def check(node1, node2):
    if (node1==None and node2==None):
        return 1
    if ((node1==None and node2!=None) or (node1!=None and node2==None)):
        return 0
    if (node1.val != node2.val):
        return 0
    if (self.check(node1.left,node2.right) and self.check(node1.right,node2.left)):
        return 1
    else:
        return 0

def isSymmetric(self, root):
    return self.check(root,root)
