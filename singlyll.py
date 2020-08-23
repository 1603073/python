class Node():
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = None

class SinglyLinkedList():
    def __init__(self,head=None):
        self.head = head

    def appendleft(self,item):
        new_node = Node(item)
        new_node.next = None
        self.head = new_node
    
    def beforehead(self,item):
        if self.head:
            b_head = Node(item)
            b_head.next = self.head
            self.head = b_head
        else:
            print('Enter the head element')    
    def append(self,item):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = Node(item)

        else:
            self.head = Node(item)
    def printlist(self):
        current = self.head 
        while current:
            print(current.item)
            current = current.next   

def main():
    n = SinglyLinkedList()
    while True:
            print('1.appendleft\n2.append\n3.beforehead\n4.display')
            print('Enter your choice: ',end='')
            case = int(input())
            if case == 1:
                print('Enter the number: ',end='')
                item = int(input())
                n.appendleft(item)
            elif case == 2:
                print('Enter the number: ',end='')
                item = int(input())
                n.append(item)
            elif case == 4:
                n.printlist()  
            elif case == 3:
                print('Enter the number: ',end='')
                item = int(input())
                if n.head:
                    n.beforehead(item) 
                else:
                    print('Enter the head element')        
            else:
                exit()         

if __name__ == "__main__":
    main()