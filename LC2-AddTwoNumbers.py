# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = None
        head = None

        while True:
            if l1 is None and l2 is None:
                break

            elif l1 is None:
                sum = l2.val + carry
                l2 = l2.next
            elif l2 is None:
                sum = l1.val + carry
                l1 = l1.next
            else:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            carry = sum / 10
            last_digit = sum % 10

            if result is None:
                result = ListNode(last_digit)
                head = result
            else:
                result.next = ListNode(last_digit)
                result = result.next

        if carry != 0:
            result.next = ListNode(carry)
        return head