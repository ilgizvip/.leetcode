#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = ''
        while l1 != None:
            s1 = str(l1.val) + s1
            l1 = l1.next
        s2 = ''
        while l2 != None:
            s2 = str(l2.val) + s2
            l2 = l2.next

        x = int(s1) + int(s2)

        next = None
        for c in str(x):
            next = ListNode(int(c), next)

        return next

# @lc code=end


