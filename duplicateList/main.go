package main

type ListNode struct {
    Val int
    Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	dummy:=ListNode{0,head}
	curr:= dummy.Next	
	for(curr.Next!=nil){		
		if(curr.Next.Val==curr.Next.Next.Val){			
			cacheVal:=curr.Next.Val
			for(curr.Next.Val==cacheVal){
				curr = curr.Next
			}			
		}else{
			curr = curr.Next
		}
	}
	return dummy.Next
}