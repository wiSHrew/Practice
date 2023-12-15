class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def get_last_value(self):
        if self.head is None:
            return None  # Empty list
        current_node = self.head
        prev_node = None
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next

        last_node = current_node.val
        if prev_node:
            prev_node.next = None
        else:
            self.head = None
        return last_node

    def reverseLL(self):
        l1_len = self.sizeOfLL()
        r_l1 = []
        for _ in range(l1_len):
            last_node = self.get_last_value()
            r_l1.append(last_node)

        return r_l1

    def addTwoNumbers(self, l1, l2):
        r_l1 = self.reverseLL()
        s_l1 = int(''.join(map(str, r_l1)))
        
        r_l2 = self.reverseLL()
        s_l2 = int(''.join(map(str, r_l2)))

        answer = s_l1 + s_l2
        answer_str = str(answer)
        
        result_list = [int(digit) for digit in answer_str[::-1]]
        
        return result_list

# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print(result)
