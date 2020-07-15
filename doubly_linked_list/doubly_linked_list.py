"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        current = self.head
        
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.prev = None
        else:
            current.next = current
            self.head = new_node
            self.head.next = current
            current.next.prev = self.head     
            
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        elif self.length == 1:
            current = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return current.value
        else:
            current = self.head
            new_Head = self.head.next
            self.head = new_Head
            self.head.prev = None
            self.length -= 1
            return current.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        elif self.length == 1:
            current = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return current.value
        else:
            current = self.tail
            new_Tail = self.tail.prev
            self.tail = new_Tail
            self.length -= 1
            return current.value

    
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return 
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is None:
            return
        elif self.tail == node:
            self.remove_from_tail()
        elif self.head == node:
            self.remove_from_head()
        else:
            
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value
        current_node = self.head

        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value

