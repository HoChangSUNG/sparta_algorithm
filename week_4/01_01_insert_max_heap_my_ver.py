class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value) # node를 입력 받을때
        parent_index = len(self.items) - 1
        child_index = len(self.items) - 1
        while parent_index > 1 :
            parent_index=child_index // 2
            if self.items[parent_index] < self.items[child_index] :
                self.items[parent_index], self.items[child_index] = self.items[child_index] , self.items[parent_index]
            else :
                break
            child_index = parent_index
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!