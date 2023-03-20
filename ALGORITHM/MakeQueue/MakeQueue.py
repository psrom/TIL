# queue 구현

class QueueList(object):
    def createQueue(self):
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)

    def dequeue(self):
        if len(self.queue) == 0:
            return 0
        else: self.queue.pop(0)

    def printQueue(self):
        print(self.queue)

Q = QueueList()
Q.createQueue()

Q.enqueue(1)
Q.printQueue()

Q.enqueue(2)
Q.printQueue()

Q.enqueue(3)
Q.printQueue()

Q.dequeue()
Q.printQueue()

Q.dequeue()
Q.printQueue()

Q.dequeue()
Q.printQueue()
