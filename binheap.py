class Node:
    def __init__(self, key, value, ):  # index):
        self.key = key
        self.value = value
        # self.index = index


class Heap:
    def __init__(self):
        self.elements = list()
        self.indexes = dict()

    def siftup(self, idx):
        while self.elements[idx].key < self.elements[((idx - 1) // 2)].key:
            if idx == 0:
                break
            idx_of_parent = (idx - 1) // 2
            self.elements[idx], self.elements[idx_of_parent] = self.elements[idx_of_parent], self.elements[idx]
            self.indexes[self.elements[idx].key], self.indexes[self.elements[idx_of_parent].key] = \
                self.indexes[self.elements[idx_of_parent].key], self.indexes[self.elements[idx].key]
            idx = (idx - 1) // 2
        # return True

    def add(self, key, value):
        if self.indexes.get(key):
            return False
        x = Node(key, value)  # , len(self.elements))
        idx = len(self.elements)
        idx_of_parent = (idx - 1) // 2
        self.indexes[key] = len(self.elements)
        self.elements.append(x)
        if idx > 0 and x.key < self.elements[idx_of_parent].key:
            self.siftup(idx)
        return True

    def set(self, key, value):
        if self.indexes.get(key):
            self.elements[self.indexes.get(key)].value = value
            return True
        else:
            return False

    def search(self, key):
        return self.elements[self.idx.get(key)].key, self.elements[self.idx.get(key)].value if self.idx.get(key) else None, None

    def min(self):
        return 'error' if len(self.elements) == 0 else (str(self.elements[0].key) + '0' + self.elements[0].value)
        # return self.elements[0]
        # eto bred

    def max(self):
        if len(self.elements) == 0:
            return 'error'
        x = max(self.elements)
        return str(x.key) + ' ' + str(self.indexes.get(x.key)) + ' ' + x.value
        # return True

    def delete(self, key):
        return True

    def heapify(self):
        return True

    def extract(self):
        return True

    def print(self):
        return True


h = Heap()
h.add(1, '11')
h.add(2, '22')