# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        current = root
        while current:
            length += 1
            current = current.next
        
        part_size = length // k      
        extra_nodes = length % k     

        parts = []
        current = root
        for i in range(k):
            part_head = current
            size = part_size + (1 if i < extra_nodes else 0)
            
            for j in range(size - 1):
                if current:
                    current = current.next
            
            if current:
                next_part = current.next
                current.next = None  
                current = next_part 
            
            parts.append(part_head)
        
        while len(parts) < k:
            parts.append(None)
        
        return parts
