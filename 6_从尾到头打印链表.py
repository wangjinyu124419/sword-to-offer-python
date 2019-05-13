"""
// 面试题6：从尾到头打印链表
// 题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
"""
class Node():
    def __init__(self,item):
        self.item=item
        self.next=None

class Chain():
    def __init__(self):
        self.head=None

    #头部添加元素
    def add(self,node_item):
        node=Node(node_item)
        if not self.head:
            self.head=node
            return
        temp_node=self.head

        self.head=node
        self.head.next=temp_node
    #尾部添加元素
    def append(self,node_item):
        node=Node(node_item)
        if not self.head:
            self.head=node
            return
        cur_node=self.head
        while cur_node.next:
            cur_node=cur_node.next
        cur_node.next=node


    #插入节点：
    def insert(self,node_item,pos):
        pass

    def get_length(self):
        length=0
        cur_node=self.head
        while cur_node:
            length+=1
            cur_node=cur_node.next
        return length

    #遍历链表
    def travel(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.item)
            cur_node=cur_node.next
    def is_empty(self):
        return self.head is None
    #反向遍历链表
    def reverse_travel(self,head_node):
        if not head_node:
            return
        self.reverse_travel(head_node.next)
        print(head_node.item)

if __name__ == '__main__':
    chain=Chain()
    # print(chain.get_length())
    # print(chain.is_empty())
    chain.append(1)
    chain.append(2)
    chain.append(3)
    chain.append(4)
    # chain.add(4)
    chain.travel()
    chain.reverse_travel(chain.head)
    # print(chain.get_length())
    # print(chain.is_empty())
