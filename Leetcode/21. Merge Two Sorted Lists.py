# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ls=[]
        if l1==None:
            return l2
        elif l2==None:
            return l1
        else:
            while l1:
                ls.append(l1.val)
                l1=l1.next
            while l2:
                ls.append(l2.val)
                l2=l2.next
            ls=sorted(ls)
            current=ListNode(ls[0])
            head=current
            for i in ls[1:]:
                temp=ListNode(i)
                current.next=temp
                current=temp
            return head