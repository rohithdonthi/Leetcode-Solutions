class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow = head
        fast = head
        prev_of_slow = None
        
        while fast and fast.next:
            fast = fast.next.next
            prev_of_slow = slow
            slow = slow.next
        
        middle = None
        if fast:
            middle = slow
            slow = slow.next
        
        second_half = slow
        prev_of_slow.next = None  
        second_half = self.reverse(second_half)

        palindrome = True
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                palindrome = False
                break
            first_half = first_half.next
            second_half = second_half.next
        
        second_half = self.reverse(second_half)
        if middle:
            prev_of_slow.next = middle
            middle.next = second_half
        else:
            prev_of_slow.next = second_half
        
        return palindrome
    
    def reverse(self, head):
        """
        Reverses the linked list and returns the new head.
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

        