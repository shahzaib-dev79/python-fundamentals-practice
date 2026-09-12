class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next   # save the next node before we overwrite it
        current.next = prev        # reverse the pointer
        prev = current             # move prev forward
        current = next_node        # move current forward

    return prev   # prev is now the new head


# --- Helper functions for testing ---
def build_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))


# --- Example usage ---
head = build_list([1, 2, 3, 4, 5])
print_list(head)                  # 1 -> 2 -> 3 -> 4 -> 5

reversed_head = reverse_list(head)
print_list(reversed_head)         # 5 -> 4 -> 3 -> 2 -> 1