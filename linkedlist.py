class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        list = self.head
        llist = ''
        
        while list:
            llist += str(list.data) + '-->'
            list = list.next
        print(llist)
    
    def addStart(self, data):
        self.head = Node(data, self.head)
        
    def addEnd(self, data):
        list = self.head
        while list.next:
            list = list.next
        list.next = Node(data,None)
        
    def addAt(self, data, index):
        list = self.head
        if(index == 0):
            self.addStart(data)
            return
        count = 0
        while list:
            if count == index-1:
                list.next = Node(data,list.next)
                break
            count += 1
            list = list.next
    def removeAt(self, index):
        list = self.head
        if(index == 0):
            self.head = self.head.next
            return
        count = 0
        while list:
            if count == index-1:
                list.next = list.next.next
                break
            count += 1
            list = list.next
        
    def listLength(self):
        list = self.head
        count = 0
        while list:
            list = list.next
            count += 1
        print(count)
        return count
        
ll = LinkedList()
ll.addStart(3)
ll.addStart(2)
ll.addEnd(4)
ll.addAt(1,0)
ll.removeAt(3)
ll.listLength()
ll.print_list()