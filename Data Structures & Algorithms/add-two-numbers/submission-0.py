class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0) # temporary starter node
        resultVal = dummy
        carryVal = 0
        while l1 or l2 or carryVal:
            currVal = 0
            currVal += carryVal
            if l1:
                currVal += l1.val
                l1 = l1.next
            if l2:
                currVal += l2.val
                l2 = l2.next
            
            carryVal = currVal // 10
            currVal = currVal % 10

            resultVal.next = ListNode(currVal)
            resultVal = resultVal.next

        return dummy.next