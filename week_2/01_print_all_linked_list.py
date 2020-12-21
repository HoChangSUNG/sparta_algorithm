#node안에는 data,next가 존재해야 함
class Node :
    def __init__(self, data):
        self.data=data
        self.next=None


first_node=Node(4)
second_node=Node(20)
first_node.next=second_node
print(first_node.data)
print(first_node.next.data)

class LinkedList:
    def __init__(self,data):
        self.head=Node(data)
    def append(self,data):
        cur=self.head
        while cur.next is not None :
            cur=cur.next
        print(cur.data)

        cur.next=Node(data)

    def print_all(self):
        cur=self.head
        while cur is not None :
            print(cur.data)
            cur=cur.next
linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()