
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

def solve(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next


        first.next = second.next
        second.next = first
        prev.next = second


        prev = first
    return dummy.next


def main():
    arr = list(map(int, input().split()))
    head = create_linked_list(arr)
    newHead = solve(head)
    print_linked_list(newHead)

main()
    