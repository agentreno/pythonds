class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)

        if self.head == None:
            self.tail = temp

        temp.setNext(self.head)
        self.head = temp


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        if current == self.tail:
            if previous == None:
                self.tail = None
            else:
                self.tail = previous


    def append(self, item):
        temp = Node(item)

        if self.tail == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.setNext(temp)
            self.tail = temp

    def insert(self, item, pos):
        pass

    def index(self, item):
        current = self.head
        found = False
        counter = 1

        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                counter += 1
                current = current.getNext()

        if found:
            return counter
        else:
            return False


    def pop(self):
        current = self.head
        previous = None
        found = False

        while not found:
            if current == None:
                return None

            if current.getNext() != None:
                previous = current
                current = current.getNext()
            else:
                found = True

        self.tail = previous
        if previous != None:
            previous.setNext(None)
        else:
            self.head = None

        return current.getData()

