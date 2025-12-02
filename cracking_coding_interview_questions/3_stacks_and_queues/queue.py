class Queue:
    def __init__(self):
        self.my_queue = list()

    def enqueue(self, item):
        self.my_queue.append(item)

    def dequeue(self):
        if len(self.my_queue) < 1:
            return None
        else:
            self.my_queue.pop(0)

    def print_queue(self):
        print(self.my_queue)

 
queue = Queue()
queue.print_queue()
queue.enqueue(14)
queue.print_queue()
queue.enqueue(43)
queue.print_queue()
queue.enqueue(573)
queue.print_queue()
queue.dequeue()
queue.print_queue()
queue.dequeue()
queue.print_queue()
queue.enqueue("fssgae")
queue.print_queue()
queue.dequeue()
queue.print_queue()