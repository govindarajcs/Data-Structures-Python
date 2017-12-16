
class Node:
    
    def __init__(self,value):
        self.value = value;
        self.next = None;
    
    def getValue(self):
        return self.value;
    
    def getNext(self):
        return self.next;
    
    def setNext(self,next):
        self.next = next;
    
    def setValue(self,value):
        self.value = value;
    
    
class Stack:
    head = None;
    count = 0;
    
    def isEmpty(self):
        return self.count == 0;
    
    def length(self):
        return self.count;
    
    def push(self,element):
        newNode = Node(element);
        if (self.count == 0):
            self.head = newNode;
            newNode.setNext(None);
        else:
            newNode.setNext(self.head);
            self.head = newNode;
        self.count+=1;
    
    def pop(self):
        if self.count == 0:
            raise ("Stack is Empty");
        else:
            node = self.head;
            self.head = self.head.getNext();
            node.setNext(None);
            self.count-=1;
    
    
    def display(self):
        node = self.head;
        if(self.isEmpty()):
            print("Queue is Empty");
        else:
            while(node.getNext()!=None):
                print(node.getValue());
                node = node.getNext();
            print(node.getValue());
    
stack = Stack();
stack.push(3);
stack.push(7)
stack.push(2);
stack.push(5);
stack.push(8);
stack.push(1);
stack.pop();
stack.pop();
stack.pop();
stack.display();