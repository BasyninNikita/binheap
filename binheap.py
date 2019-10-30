class Heap:
    def __init__(self):
        self.elements = list()
        self.idx = dict()

    def add(self, key,value):
        if self.idx.get(key) != 0:
            return 'error'
        self.elements.append([key,value])
        self.idx[key] = len(self.elements) - 1
        #siftup
        return ''
    def delete(self, key):
        return True

    def min(self):
        return self.elements[0]
        #eto bred

    def max(self):
        return True

    def set(self, key, value):
        return True

    def search(self, key):
        return True

    def extract(self):
        return True

    def print(self):
        return True



h = Heap()
