class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class DoubleNode(Node):
    def __init__(self, initdata):
        Node.__init__(self, initdata)
        self.prev = None

    def getPrev(self):
        return self.prev

    def setPrev(self, newprev):
        self.prev = newprev


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        new_node = Node(item)

        # The first addition becomes and stays the tail
        if self.head == None:
            self.tail = new_node

        # New nodes are added at the head for speed
        new_node.setNext(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        # Keep a previous node pointer to join the list around the removal
        current = self.head
        previous = None
        found = False

        # Locate the matching item (assume it exists)
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # Item to remove was at the head, change head to next item
        if previous == None:
            self.head = current.getNext()
        else:
            # Join the list around the removal to remove it
            previous.setNext(current.getNext())

        # Maintain the tail pointer
        if current == self.tail:
            if previous == None:
                self.tail = None
            else:
                self.tail = previous

    def append(self, item):
        new_node = Node(item)

        # Use the tail pointe to avoid list traversal for append
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.setNext(new_node)
            self.tail = new_node

    def insert(self, item, position):
        new_node = Node(item)

        if self.head == None:
            self.head = new_node
            return

        # Find the nodes on either side of the insertion point
        counter = 0
        behind = None
        ahead = self.head
        while counter < position:
            behind = ahead
            ahead = ahead.getNext()
            counter += 1

        if behind != None:
            behind.setNext(new_node)
        else:
            self.head = new_node

        if ahead != None:
            new_node.setNext(ahead)

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

        # Traverse to the end of the list with two pointers
        while not found:
            if current == None:
                return None

            if current.getNext() != None:
                previous = current
                current = current.getNext()
            else:
                found = True

        # Update the tail and unlink the last node
        self.tail = previous
        if previous != None:
            previous.setNext(None)
        else:
            self.head = None

        return current.getData()

class OrderedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                # Assume items are integers
                # Search complexity reduced in ordered lists
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False

        # Add complexity increases as items can't just be added at the head
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        new_node = Node(item)
        # Insertion point must be at the beginning
        if previous == None:
            # Link to current head if it exists
            if current != None:
                new_node.setNext(self.head)

            self.head = new_node
        else:
            # Join nodes around the new node to insert
            new_node.setNext(current)
            previous.setNext(new_node)

        self.count += 1

    def isEmpty(self):
        return self.head == None
 
    def size(self):
        # Reduce size() complexity by storing count
        return self.count
 
    def remove(self, item):
        previous = None
        current = self.head
        stop = False

        while current != None and not stop:
            if current.getData() == item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        if current == None:
            # Item doesn't exist
            return False
        elif previous == None:
            # Item is at the head
            self.head = current.getNext()
        else:
            # Item is within the list, join around
            previous.setNext(current.getNext())

        self.count -= 1
 
    def index(self, item):
        current = self.head
        stop = False
        count = 1

        while current != None and not stop:
            if current.getData() == item:
                stop = True
            else:
                count += 1
                current = current.getNext()

        return count

 
    def pop(self):
        current = self.head
        previous = None
        stop = False
        
        # Find the end of the list and keep two pointers
        while current != None and not stop:
            if current.getNext() == None:
                stop = True
            else:
                previous = current
                current = current.getNext()

        # Unlink the last element
        previous.setNext(None)
        self.count -= 1
        return current.getData()


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        # Unordered list, just add new nodes at the head
        new_node = DoubleNode(item)
        if self.head:
            new_node.setNext(self.head)
            self.head.setPrev(new_node)

        self.head = new_node

    def remove(self, item):
        current = self.head

        # No need to maintain two pointers with backward links
        while current != None:
            if current.getData() == item:
                current.getPrev().setNext(current.getNext())
            current = current.getNext()

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head

        # List traversal required where count not maintained by list
        while current != None:
            current = current.getNext()
            count += 1

    def append(self, item):
        new_node = DoubleNode(item)
        current = self.head

        if current == None:
            self.head = new_node
            return

        # Find the last element, only one pointer needed with backwards links
        while current.getNext() != None:
            current = current.getNext()

        # Join the new node on to the tail
        new_node.setPrev(current)
        current.setNext(new_node)

    def index(self, item):
        count = 1
        current = self.head

        while current != None:
            if current.getData() == item:
                return count
            else:
                current = current.getNext()

    def insert(self, pos, item):
        new_node = DoubleNode(item)
        count = 0
        current = self.head

        # Find the insertion point
        while count < pos and current != None:
            current = current.getNext()
            count += 1

        if current == None:
            self.head = new_node
        else:
            # Link new node to previous and current
            new_node.setPrev(current.getPrev())
            new_node.setNext(current)
            # Update the previous and current nodes
            current.getPrev().setNext(new_node)
            current.setPrev(new_node)

    def pop(self):
        current = self.head

        while current.getNext() != None:
            current = current.getNext()

        if current == None:
            # The list is empty
            return None
        elif current.getPrev() == None:
            # The list had one element
            self.head = None
        else:
            # The list had more than one, update the tail's next pointer
            current.getPrev().setNext(None)

        return current.getData()
