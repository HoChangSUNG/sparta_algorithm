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

    def get_kth_node_from_last(self, k):  # 잘못 만듦. 리스트링크드가 한개일때 생각 안함.
        cur=self.head
        last_index = 0
        while cur.next is not None : #리턴해야 하는 node의 인덱스를 찾는다
            cur = cur.next
            last_index += 1

        kth_index = last_index-(k-1)#리턴해야 하는 node의 인덱스
        cur_index = 0
        cur = self.head
        while kth_index > cur_index:#index를 이용하여  해당 node 찾기
            cur = cur.next
            cur_index += 1
        return cur



linked_list = LinkedList(6)
#linked_list.append(7)
#linked_list.append(8)
print(linked_list.get_kth_node_from_last(0).data)  # 7이 나와야 합니다!