#question number one
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> " if current.next else "")
            current = current.next
        print()

linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list:")
linked_list.print_list()


linked_list.reverse()

print("Reversed linked list:")
linked_list.print_list()

#question number two
def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

#question number three
class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.head = self.tail = -1
        self.size = k

    def enqueue(self, value):
        if (self.tail + 1) % self.size == self.head:
            return False  # Queue is full
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def dequeue(self):
        if self.head == -1:
            return -1  # Queue is empty
        result = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1  # Queue is now empty
        else:
            self.head = (self.head + 1) % self.size
        return result

    def front(self):
        return -1 if self.head == -1 else self.queue[self.head]

    def rear(self):
        return -1 if self.tail == -1 else self.queue[self.tail]

    def isEmpty(self):
        return self.head == -1

q = CircularQueue(3)
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.dequeue())
print(q.enqueue(4))
print(q.front())
print(q.rear())

#question number four
def find_maximum(arr):
    return max(arr)

arr = [1, 2, 3, 4, 5]
print(find_maximum(arr))

#question number five
def reverse_string(s):
    stack = list(s)
    reversed_s = []
    while stack:
        reversed_s.append(stack.pop())
    return ''.join(reversed_s)

s = "hello"
print(reverse_string(s))



