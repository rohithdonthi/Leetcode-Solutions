class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None  
        current = head   
        
        while current:   
            next_node = current.next  
            current.next = previous   
            previous = current       
            current = next_node       
        
        return previous