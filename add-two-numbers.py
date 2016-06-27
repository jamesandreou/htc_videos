# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = str(self.sumList(l1) + self.sumList(l2))    
        iter = ListNode(int(sum[-1]))
        root = iter
        for c in reversed(sum[:-1]):
            iter.next = ListNode(int(c))
            iter = iter.next
            
        return root
        
    def sumList(self, l):
        sum = 0
        multiplier = 1
        while(l is not None):
            sum += multiplier * l.val
            multiplier *= 10
            l = l.next
        return sum
