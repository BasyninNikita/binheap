import sys


def get_command(binheap):
    for line in sys.stdin:
        if 'set' in line and line.split()[0] == 'set':
            if len(line.replace('set', '').strip().split(' ')) == 2:
                success = binheap.set(int(line.split()[1]), line.split()[2])
                if not success:
                    print('error')
            else:
                print('error')
        elif 'add' in line and line.split()[0] == 'add':
            if len(line.replace('add', '').strip().split(' ')) == 2:  # maybe isdigit
                success = binheap.add(int(line.split()[1]), line.split()[2])
                if not success:
                    print('error')
            else:
                print('error')
        elif 'search' in line and line.split()[0] == 'search':
            if len(line.replace('search', '').strip().split(' ')) == 1:
                print(stree.search(int(line.split()[1])))
            else:
                print('error')
        elif 'print' in line:
            if line.replace("print", '') != '\n':
                print('error')
            else:
                print(stree.print(), end='')
        elif 'delete' in line and line.split()[0] == 'delete':
            if len(line.replace('delete', '').strip().split(' ')) == 1:
                success = stree.delete(int(line.split()[1]))
                if not success:
                    print('error')
            else:
                print('error')
        elif 'min' in line:
            if line.replace("min", '') != '\n':
                print('error')
            else:
                print(stree.findMin())
        elif 'max' in line:
            if line.replace("max", '') != '\n':
                print('error')
            else:
                print(stree.findMax())
        elif line == '\n':
            continue
        else:
            print('error')


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
        return self.elements[self.idx.get(key)].key, self.idx.get(key), self.elements[self.idx.get(key)].value if self.idx.get(
            key) else None, None, None
        # a = search(11)
        # if a[0] is None:
        #     print('sasi')
        # else:
        #     print(a[0]+ ' ' + a[1] + ' ' + a[2])
    def min(self):
        return None, None, None if len(self.elements) == 0 else self.elements[0].key, 0, self.elements[0].value
        # return self.elements[0]
        # eto bred

    def max(self):
        if len(self.elements) == 0:
            return None, None, None
        x = max(self.elements)
        return x.key, self.indexes.get(x.key), x.value
        # return True

    def heapify(self, idx):
        while 2 * idx + 1 < len(self.elements):
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            min_child = idx
            if right_child < len(self.elements) and self.elements[right_child] < self.elements[left_child]:
                min_child = right_child
            elif right_child < len(self.elements) and self.elements[right_child] > self.elements[left_child]:
                min_child = left_child
            else:
                min_child = left_child
            if min_child == idx:
                break
            self.elements[idx], self.elements[min_child] = self.elements[min_child], self.elements[idx]
            self.indexes[self.elements[idx].key], self.indexes[self.elements[min_child].key] = \
                self.indexes[self.elements[min_child].key], self.indexes[self.elements[idx].key]
            idx = min_child

    def delete(self, key):

        return True

    def extract(self):
        return True

    def print(self):
        return True


h = Heap()
h.add(1, '11')
h.add(2, '22')
