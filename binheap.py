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
                succ = binheap.search(int(line.split()[1]))
                print('0') if succ is None else print(str(succ[0]) + ' ' + str(succ[1]) + ' ' + succ[2])
            else:
                print('error')
        elif 'print' in line:
            if line.replace("print", '') != '\n':
                print('error')
            else:
                print(binheap.print())
        elif 'delete' in line and line.split()[0] == 'delete':
            if len(line.replace('delete', '').strip().split(' ')) == 1:
                success = binheap.delete(int(line.split()[1]))
                if not success:
                    print('error')
            else:
                print('error')
        elif 'extract' in line and line.split()[0] == 'extract':
            if line.replace("extract", '') != '\n':
                print('error')
            else:
                succ = binheap.extract()
                print('error') if succ is None else print(str(succ[0]) + ' ' + succ[1])
        elif 'min' in line:
            if line.replace("min", '') != '\n':
                print('error')
            else:
                succ = binheap.min()
                print('error') if succ is None else print(str(succ[0]) + ' ' + str(succ[1]) + ' ' + succ[2])
        elif 'max' in line:
            if line.replace("max", '') != '\n':
                print('error')
            else:
                succ = binheap.max()
                print('error') if succ is None else print(str(succ[0]) + ' ' + str(succ[1]) + ' ' + succ[2])
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
        while self.elements[idx].key < self.elements[((idx - 1) // 2)].key:  # and idx > 0:
            if idx == 0:
                break
            idx_of_parent = (idx - 1) // 2
            self.elements[idx], self.elements[idx_of_parent] = self.elements[idx_of_parent], self.elements[idx]
            self.indexes[self.elements[idx].key], self.indexes[self.elements[idx_of_parent].key] = \
                self.indexes[self.elements[idx_of_parent].key], self.indexes[self.elements[idx].key]
            idx = (idx - 1) // 2

        # return True

    def add(self, key, value):
        if self.indexes.get(key) is not None:
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
        if self.indexes.get(key) is not None:
            self.elements[self.indexes.get(key)].value = value
            return True
        else:
            return False

    def search(self, key):
        if self.indexes.get(key) is not None:
            return 1, self.indexes.get(key), self.elements[self.indexes.get(key)].value
        else:
            return None
        # return 1, self.indexes.get(key), self.elements[self.indexes.get(key)].value if self.indexes.get(key) is not
        # None else None, None, None a = search(11) if a[0] is None: print('sasi') else: print(a[0]+ ' ' + a[1] + ' '
        # + a[2])

    def min(self):
        if len(self.elements) == 0:
            return None
        return self.elements[0].key, 0, self.elements[0].value
        # return None if len(self.elements) == 0 else self.elements[0].key, 0, self.elements[0].value

    def max(self):
        if len(self.elements) == 0:
            return None
        max_el = self.elements[0]
        for i in self.elements:
            if i.key > max_el.key:
                max_el = i
        return max_el.key, self.indexes.get(max_el.key), max_el.value
        # return True

    def heapify(self, idx):
        while 2 * idx + 1 < len(self.elements):
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            #min_child = left_child
            if right_child<len(self.elements):
                min_child = left_child if self.elements[left_child].key < self.elements[right_child].key else right_child
            else:
                min_child = left_child
            if self.elements[idx].key < self.elements[min_child].key:
                break
            # if left_child < len(self.elements) and self.elements[left_child].key < self.elements[min_child].key:
            #     min_child = left_child
            # if right_child < len(self.elements) and self.elements[right_child].key < self.elements[min_child].key:
            #     min_child = right_child
            # if min_child == idx:
            #     break
            self.elements[idx], self.elements[min_child] = self.elements[min_child], self.elements[idx]
            self.indexes[self.elements[idx].key], self.indexes[self.elements[min_child].key] = \
                self.indexes[self.elements[min_child].key], self.indexes[self.elements[idx].key]
            idx = min_child



    def delete(self, key):
        if len(self.elements) == 0 or self.indexes.get(key) is None:
            return False
        idx = self.indexes.get(key)
        if idx == len(self.elements) - 1:
            self.elements.pop()
            self.indexes.pop(key)
            return True
        self.elements[idx], self.elements[(len(self.elements) - 1)] = self.elements[(len(self.elements) - 1)], \
                                                                      self.elements[idx]
        self.indexes[self.elements[idx].key] = idx
        xkey = self.elements[idx].key
        ykey = self.elements[len(self.elements) - 1].key
        self.elements.pop()
        self.siftup(idx)
        self.heapify(self.indexes.get(xkey))
        self.indexes.pop(ykey)  # self.indexes.get(ykey))
        return True

    def extract(self):
        if len(self.elements) == 0:
            return None
        key = self.elements[0].key
        value = self.elements[0].value
        self.delete(self.elements[0].key)
        return key, value

    def print(self):
        if len(self.elements) == 0:
            return '_'
        printed = 0  # printed_nodes
        level = 0
        s = ''
        for i in self.elements:
            s += '[' + str(i.key) + ' ' + i.value
            if self.indexes.get(i.key) != 0:
                s += ' ' + str(self.elements[(self.indexes.get(i.key) - 1) // 2].key) + ']'
            else:
                s += ']'
            printed += 1
            if printed == (1 << level):
                s += '\n'
                level += 1
                printed = 0
            else:
                s += ' '
        # k = 2 ** level
        if printed != 0:
            for i in range(((1 << level) - printed)):  # - len(self.elements))):
                s += '_ '
        # while printed < 2 ** (int(log2(len(self.elements))) + 1):
        #     s += ' _'
        return s.rstrip()


h = Heap()
get_command(h)
# h.add(1, '11')
# h.add(2, '22')
# h.set(1, '12')
# print(h.search(1))
# print(h.min())
# #h.delete(1)
# print(h.search(1))
# #print(h.extract())
