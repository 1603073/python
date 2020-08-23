a = []
class Stack:
    def __init__(self):
        self.a = []

    def push(self,item):
        return self.a.append(item)

    def size(self):
        return len(self.a)   

    def is_empty(self):
        if self.size() > 0:
            return False 
        else:
            return True   
    def pop(self):
        if self.is_empty():
            print('the stack is empty')
        return self.a.pop()
    def exit(self):
        return('the choice is not between 1 to 4')     

def main():
     s = Stack()
     while True:
        print('1.push\n2.pop\n3.display\n4.exit')
        print('Enter your choice: ',end='')
        case = int(input())
        if case == 1:
            print('Enter the item: ',end='')
            item = int(input())
            print(s.push(item))  
        elif case == 2:
                if(s.size()==0):
                    print('স্ট্যাকটি ফাঁকা')
                else:    
                    print('The popping element is :', s.pop())
        elif case == 3:
                if(s.size() == 0):
                    print('the stack is empty')
                else:
                    print(s.a)    
        else:
                print(s.exit())
                exit()

if __name__ == "__main__":
    main()

                      
                          