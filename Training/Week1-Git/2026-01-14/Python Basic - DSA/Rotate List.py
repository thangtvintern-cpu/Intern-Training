import sys
class Node():
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    dummy = Node()
    curr = dummy
    for val in arr:
        curr.next = Node(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next

def solve(head, k):
    if head == None or head.next == None:
        return head
    prev = head
    newHead = head
    for i in range(k):
        while prev.next.next != None:
            prev = prev.next
        prev.next.next = newHead
        newHead = prev.next
        prev.next = None
        prev = newHead    
    return newHead
            
        

    
def main():
    data = sys.stdin.read().strip().splitlines()
    arr = list(map(int, data[0].split()))
    k = int(data[1])
    head = create_linked_list(arr)
    newHead = solve(head, k)
    print_linked_list(newHead)

main()