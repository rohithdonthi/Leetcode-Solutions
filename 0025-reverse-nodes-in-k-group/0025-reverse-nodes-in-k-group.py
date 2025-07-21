class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def hasKNodes(curr, k):
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            return count == k

        def reverseK(curr, k):
            prev = None
            tail = curr
            while k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            return prev, tail, curr 

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        curr = head

        while hasKNodes(curr, k):
            rev_head, rev_tail, next_group_head = reverseK(curr, k)
            group_prev.next = rev_head
            rev_tail.next = next_group_head
            group_prev = rev_tail
            curr = next_group_head 

        return dummy.next

