class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur=self.head
        for i in range(index) :
            cur=cur.next

        return cur

    def add_node(self, index, value):
        count=0
        node=self.head
        while node is not None :
            if count+1==index :#추가할 value의 인덱스가 0이 아닐때
                tmp=node.next
                node.next=Node(value)
                node=node.next
                node.next=tmp
                break
            node=node.next
            count+=1
        else : #추가할 value의 인덱스가 0일때
            tmp=self.head
            self.head=Node(value)
            self.head.next=tmp


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(2, 3)
linked_list.print_all()