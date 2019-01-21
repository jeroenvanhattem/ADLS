"""
Jeroen van Hattem
1675180
TICT-TI-V2A
Joop Kaldeway
"""
class ListNode:
    """
    Definition
        Initialize the list node with data and the next node
    
    Parameters
    ----------
    data : item
        The data that the node contains
    next : ListNode
        The next node
    """
    def __init__(self,data,next):
        self.data = data
        self.next = next

    """
    Definition
        The way the node will be printed
    """
    def __repr__(self):
        return str(self.data)

class MyCircularLinkedList:
    """
    Definition
        Set the tail to None
    """
    def __init__(self):
        self.tail = None

    """
    Definition
        The way the node will be printed. As long this node is not the last node, it will print " -> " plus the next node
    """
    def __repr__(self):
        s = ''
        list_to_be_printed = []
        if not self.tail:
            s = "Empty"
        else:
            current = self.tail
            while current.next != self.tail:
                list_to_be_printed.insert(0, str(current.data))
                if current != self.tail:
                    list_to_be_printed.insert(1, " -> ")
                current = current.next
            list_to_be_printed.insert(0, str(current))
            if current != self.tail:
                list_to_be_printed.insert(1, " -> ")
        for x in list_to_be_printed :
            s += x
        return s

    """
    Definition
        Add the passed parameter to the end
    
    Parameters
    ----------
    e : item
        Make a ListNode with e and use it as the tail
    """
    def append(self, e):
        if not self.tail:
            self.tail = ListNode(e, None)
            self.tail.next = self.tail
        else:
            current = self.tail
            while current.next != self.tail:
                current = current.next

            x =ListNode(e, None)
            x.next = self.tail
            current.next = x
            self.tail = current.next

    """
    Definition
        Delete the node containing the passed parameter from the list
    
    Parameters
    ----------
    e : item
        Node to be deleted
    """
    def delete(self,e):
        if not self.tail:
            print("Can't delete node, list is empty")
        else:
            current = self.tail
            backup = None

            if current.next == self.tail:
                self.tail = None
            else:
                while current.data != e:
                    if current.next == self.tail:
                        print("Node not found")
                    else:
                        backup = current
                        current = current.next

                if current == self.tail:
                    backup = self.tail
                    while backup.next != self.tail:
                        backup = backup.next

                    self.tail = self.tail.next
                    backup.next = self.tail
                else:
                    if current.next == self.tail:
                        backup.next = self.tail
                    else:
                        backup.next = current.next

    

mylist = MyCircularLinkedList()
print(mylist)
mylist.append(1)
print(mylist)
mylist.append(2)
print(mylist)
mylist.append(3)
print(mylist)
mylist.append(4)
print(mylist)
mylist.append(5)
print(mylist)
mylist.delete(5)
print(mylist)
mylist.delete(1)
print(mylist)
mylist.delete(3)
print(mylist)
mylist.delete(4)
print(mylist)
mylist.delete(2)
print(mylist)






































