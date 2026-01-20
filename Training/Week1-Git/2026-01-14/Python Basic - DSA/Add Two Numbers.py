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

def combine_numbers(head)->int:
    dummy = Node()
    dummy.next = head
    cur = dummy
    list_number = []
    while cur.next:
        if cur.next.val != 0:
            list_number.append(cur.next.val)
        cur = cur.next
    result = int("".join(map(str, list_number[::-1])))
    return result

def main():
    data = sys.stdin.read().strip().splitlines()

    list1 = list(map(int,data[0].split()))
    list2 = list(map(int,data[1].split()))

    node1 = create_linked_list(list1)
    node2 = create_linked_list(list2)
    result = combine_numbers(node1) + combine_numbers(node2)
    final_list = []
    while result > 0:
        final_list.append(result % 10)
        result = result // 10
    print_linked_list(create_linked_list(final_list))

main()