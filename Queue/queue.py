# queue using list


class Queue:
    def __init__(self):
        self.mylist = []
        self.item_count = 0


    def is_empty(self):
        return len(self.mylist)==0

    def enqueue(self, data):
        self.mylist.append(data)
        self.item_count +=1

    def dequeue(self):
        if not self.is_empty():
            self.mylist.pop(0)
            self.item_count -= 1
        else:
            IndexError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError('Queue Underflow')

    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError('Queue Underflow')

    def size(self):
        return self.item_count
