a = []
class Queue:
    def __init__(self):
        self.a = []

    def enqueue(self,item):
        return self.a.append(item)

    def size(self):
        return len(self.a)   

    def is_empty(self):
        if self.size() > 0:
            return False 
        else:
            return True   
    def dequeue(self):
        if self.is_empty():
            print('the queue is empty')
        else:
            return self.a.pop(0)
    def exit(self):
        return('the choice is not between 1 to 4')     

def main():
     s = Queue ()
     while True:
        print('1.enqueue\n2.dequeue\n3.display\n4.exit')
        print('Enter your choice: ',end='')
        case = int(input())
        if case == 1:
            print('Enter the item: ',end='')
            item = int(input())
            print(s.enqueue(item))  
        elif case == 2:
                if(s.size()==0):
                    print('স্ট্যাকটি ফাঁকা')
                else:    
                    print('The popping element is :', s.dequeue())
        elif case == 3:
                if(s.size() == 0):
                    print('the queue is empty')
                else:
                    print(s.a)    
        else:
                print(s.exit())
                exit()

if __name__ == "__main__":
    main()

                      
                          