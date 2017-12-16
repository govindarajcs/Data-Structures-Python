class Node:
    
    def __init__(self,value):
        self.value = value;
        self.next = None;
        
    def setNext(self,newNext):
        self.next = newNext;
        
    def setValue(self,newValue):
        self.value = newValue;
    
    def getNext(self):
        return self.next;
    def getValue(self):
        return self.value;


class LinkedList:
    head = None;
    tail = None;
    count = 0;
    def insertFirst(self,element):
        newNode = Node(element);
        if (self.count==0):
            newNode.setNext(None);
            self.head = self.tail = newNode;
        else:
            newNode.setNext(self.head);
            self.head = newNode;
        self.count+=1;
    
    def display(self):
        node = self.head;
        if(self.isEmpty()):
            print("Queue is Empty");
        else:
            while(node.getNext()!=None):
                print(node.getValue());
                node = node.getNext();
            print(node.getValue());
    
    def insertLast(self,element):
        newNode = Node(element);
        if (self.count==0):
            newNode.setNext(None);
            self.head=self.tail=newNode;
        else:
            self.tail.setNext(newNode);
            newNode.setNext(None);
            self.tail = newNode;
        self.count+=1;
        
    def insertAt(self,element,position):        
        if(position>0):
            newNode = Node(element);
            newNode.setNext(None);
            count = 0;
            node = self.head;
            while(count<(position-1)):
                node = node.getNext();
                count+=1;
            newNode.setNext(node.getNext());
            node.setNext(newNode);
            self.count+=1;
        else:
            self.insertFirst(element);

    def deleteLast(self):
        if(self.count>0):
            node = self.head;
            count = 1;
            while (count<self.count-1):
                node = node.getNext();
                count+=1;
            node.setNext(None);
            self.count-=1;
        
    def deleteFirst(self):
        node = self.head;
        self.head = node.getNext();
        node.setNext(None);
    
    def deleteAt(self,position):
        node = self.head;
        count = 0;
        while(count<(position-1)):
            count+=1;
            node=node.getNext();
        delNode = node.getNext();
        node.setNext(delNode.getNext());
        delNode.setNext(None);
        self.count-=1;
    
    def isEmpty(self):
        return self.head == None;
    
    def length(self):
        return self.count;
        
        
linkedList = LinkedList();
linkedList.insertFirst(3);
linkedList.insertFirst(5);
linkedList.insertLast(9);
linkedList.insertLast(8);
linkedList.insertAt(6, 1);
linkedList.insertAt(7, 3);
linkedList.deleteLast();
linkedList.deleteFirst();
linkedList.deleteAt(1);
linkedList.display();