__author__ = 'effy'
'''
merge k sorted linked list, return as one. Analyze time complexity

thought:
divide and conquer
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists_TLE(self, lists):
        l = len(lists)
        if l == 1:
            return lists[0]
        if l == 0:
            return None
        while l > 1:
            merged = self.mergeTwoLists(lists[-1],lists[-2])
            lists.pop()
            lists[-1] = merged
            l = len(lists)
        return lists[0]

    def mergeKLists(self, lists):
        l = len(lists)
        if l == 1:
            return lists[0]
        if l == 0:
            return None
        prev_list = lists
        while l > 1:
            nextList = []
            for i in range(0, l-1, 2):
                merged = self.mergeTwoLists(prev_list[i],prev_list[i+1])
                nextList.append(merged)
            if l%2: nextList.append(prev_list[-1])
            l = len(nextList)
            prev_list = nextList
        return nextList[0]


    def mergeTwoLists(self, listA, listB):
        dummy = ListNode(0)
        curA, curB, cur = listA, listB,dummy
        while curA and curB:
            if curA.val <= curB.val:
                cur.next = curA
                curA = curA.next
            else:
                cur.next = curB
                curB = curB.next
            cur = cur.next
        if curA:
            cur.next = curA
        if curB:
            cur.next = curB
        return dummy.next


