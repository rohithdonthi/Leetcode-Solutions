class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        old = head
        new = head.next
        new_head = head.next

        while old:
            old_next = old.next.next
            new_next = new.next.next if new.next else None
            old.next = old_next
            new.next = new_next
            old = old_next
            new = new_next

        return new_head