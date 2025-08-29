import sys, os, io, atexit
# TODO: list 등으로 최적화 해보기

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

class Node:
    __slots__ = ('val', 'before','next')

    def __init__(self, val):
        self.val = val
    
    def add_next(self, next):
        self.next = next

    def add_before(self, before):
        self.before = before
    
    def print_val(self):
        print(self.val)

class Double_Linked_list:
    def __init__(self, node):
       self.head = node
       self.tail = node
       self.dict = {}
       self.dict[node.val] = node
    
    def add_node(self, node):
        self.tail.add_next(node)
        node.add_before(self.tail)
        self.tail = node
        self.dict[node.val] = node
    
    def find_val(self, val):
        node = self.dict.get(val, None)
        return node
    
    def insert_after(self, i, j):
        node = self.find_val(i)
        if node is not None:
            next_node = node.next
            next_node.print_val()

            new_node = Node(j)

            node.add_next(new_node)
            new_node.add_before(node)

            new_node.add_next(next_node)
            next_node.add_before(new_node)

            self.dict[j] = new_node
    
    def insert_before(self, i, j):
        node = self.find_val(i)
        if node is not None:
            before_node = node.before
            before_node.print_val()

            new_node = Node(j)

            node.add_before(new_node)
            new_node.add_next(node)

            new_node.add_before(before_node)
            before_node.add_next(new_node)

            self.dict[j] = new_node
    
    def delete_after(self, i):
        node = self.find_val(i)
        if node is not None:
            next_node = node.next
            next_node.print_val()
            node.add_next(next_node.next)
            next_node.next.add_before(node)
            del self.dict[next_node.val]
    
    def delete_before(self, i):
        node = self.find_val(i)
        if node is not None:
            before_node = node.before
            before_node.print_val()
            node.add_before(before_node.before)
            before_node.before.add_next(node)
            del self.dict[before_node.val]
    
    def traverse(self):
        now = self.head
        while True:
            now.print_val()
            now = now.next
            if now.val == self.head.val:
                break

def run_program():
    N, M = map(int, input().strip().split())
    stations = list(map(int, input().strip().split()))
    dl_list = Double_Linked_list(Node(stations[0]))
    for i in range(1, N):
        dl_list.add_node(Node(stations[i]))
    dl_list.head.add_before(dl_list.tail)
    dl_list.tail.add_next(dl_list.head)
    for _ in range(M):
        commands = input().strip().split()
        if commands[0] == 'BN':
            dl_list.insert_after(int(commands[1]), int(commands[2]))
        elif commands[0] == 'BP':
            dl_list.insert_before(int(commands[1]), int(commands[2]))
        elif commands[0] == 'CN':
            dl_list.delete_after(int(commands[1]))
        elif commands[0] == 'CP':
            dl_list.delete_before(int(commands[1]))

run_program()

