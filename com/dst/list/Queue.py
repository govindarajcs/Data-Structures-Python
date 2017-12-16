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
        
    
class Queue:
    
    head = None;
    rear = None;
    count = 0;
    
    def add(self,element):
        newNode = Node(element);
        newNode.setNext(None);
        if(self.count == 0):
            self.head = self.rear = newNode;
        else:
            self.rear.setNext(newNode);
            self.rear = newNode;
        self.count+=1;
    
    def remove(self):
        if(self.count == 0):
            raise("Queue is Empty");
        else:
            node = self.head;
            self.head = node.getNext();
            node.setNext(None);
            self.count-=1;
        
    def length(self):
        return self.count;
    
    def isEmpty(self):
        return self.count == 0;
    
    
    def display(self):
        node = self.head;
        if(self.isEmpty()):
            print("Queue is Empty");
        else:
            while(node.getNext()!=None):
                print(node.getValue());
                node = node.getNext();
            print(node.getValue());
    
    
queue = Queue();
queue.add(2);
queue.add(3);
queue.add(4);
queue.add(5);
queue.add(6);
queue.add(7);
queue.remove();
queue.remove();
queue.remove();
queue.remove();
queue.remove();
queue.remove();
queue.display();