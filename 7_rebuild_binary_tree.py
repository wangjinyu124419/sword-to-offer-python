class Node():
    def __init__(self,item=None):
        self.item=item
        self.lchild=None
        self.rchild=None
    def __str__(self):
        return str(self.item)

class Tree():
    def __init__(self,root=None):
        self.root=root
    #添加节点
    def add_node(self,item):
        node=Node(item)
        if not self.root:
            self.root=node
        node_list=[]
        node_list.append(node)
        while node_list:
            cur_node=node_list.pop(0)
            if not cur_node.lchild:
                cur_node.lchild=cur_node
                return
            if not cur_node.rchild:
                cur_node.rchild=cur_node
                return
            node_list.append(cur_node.lchild)
            node_list.append(cur_node.rchild)

    def preorder(self,root):
        if not root:
            return
        print(root.item)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.lchild)
        print(root.item)
        self.inorder(root.rchild)

    def postorder(self,root):
        if not root:
            return

        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.item)

def rebuild_btree(preorder,inorder,root):

    if (not preorder) or (not inorder):
        return None
    if not root.item:
        root.item=preorder[0]
    # print(root)
    index=inorder.index(preorder[0])
    l_inorder=inorder[:index]
    r_inorder=inorder[index+1:]
    l_preorder=preorder[1:len(l_inorder)+1]
    r_preorder=preorder[len(l_inorder)+1:]
    if l_preorder:
        root.lchild=Node(l_preorder[0])
        rebuild_btree(l_preorder, l_inorder, root.lchild)

    if r_preorder:
        root.rchild=Node(r_preorder[0])
        rebuild_btree(r_preorder,r_inorder,root.rchild)


def fun(node):
    if not node:
        node=Node(1)
    return node.item

if __name__ == '__main__':
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    node=Node()
    rebuild_btree(preorder,inorder,node)

    tree=Tree(node)
    # print(tree.root.lchild.rchild)
    # print(tree.root.rchild.rchild.lchild)
    # tree.preorder(tree.root)
    # tree.inorder(tree.root)
    tree.postorder(tree.root)

