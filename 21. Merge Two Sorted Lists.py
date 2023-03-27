Solution 1:-------------------

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        n=node
        while(list1!=None and list2!=None):
            if(list1.val<=list2.val):
                n.next=list1
                list1=list1.next
                n=n.next
            else:
                n.next=list2
                list2=list2.next
                n=n.next
        if(list1!=None):
            n.next=list1
        else:
            n.next=list2
        return node.next

Solution 2:-------------------

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur=new=ListNode()
        while list1 and list2:
            if list1.val < list2.val :
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        if list1 or list2 :
            cur.next = list1 if list1 else list2
        return new.next



        
