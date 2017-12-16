'''
Created on 09-Dec-2017

@author: DELL
'''

import gc;
from pip._vendor.distlib.compat import raw_input
from builtins import print
from pip._vendor.requests.api import options

class MyClass(object):
    '''
    classdocs
    '''
    numberlist = []
    count = 0;
    def __init__(self, x):
        '''
        Constructor
        '''
        self.numberlist = x;
    
    def insertLast(self,element):
        number=[element];
        self.numberlist+=number;
        self.count+=1;
    
    def insertFirst(self,element):
        number = [element];
        self.numberlist = number+self.numberlist;
        self.count+=1;
        
    def length(self):
        return self.count;
    
    def insertAt(self,element,position):
        temp1=[self.numberlist[self.length()-1]];
        for i in range(self.length()-1,position,-1):
            self.numberlist[i] = self.numberlist[i-1];
        self.numberlist[position] = element;
        self.numberlist+=temp1;
        self.count+=1;
        
    def deleteAt(self,position):
        for i in range(position+1,self.length(),1):
            self.numberlist[i-1] = self.numberlist[i];
        self.numberlist[self.length()-1] = None;
        gc.enable();
        self.count-=1;
    
    def isEmpty(self):
        return self.count==0;
            
    
    def deleteLast(self):
        
        self.numberlist[self.length()-1] = None;
        self.count-=1;
    
    def deleteFirst(self):
        for i in range(1,self.length(),1):
            self.numberlist[i-1] = self.numberlist[i];
        self.numberlist[self.length()-1] = None;
        self.count-=1;
        
    def search(self,element):
        for i in range(0,self.length(),1):
            if (element == self.numberlist[i]):
                return i;
        return -1;
    
    def display(self):
        for i in range(0,self.length(),1):
            print(self.numberlist[i]);

listnumbers = [];
numbersObject = MyClass(listnumbers);


def switch(value):
    options ={
            1:lambda:numbersObject.insertFirst(int(raw_input())),
            2:lambda:numbersObject.insertAt(int(raw_input()),int(raw_input())),
            3:lambda:numbersObject.deleteLast(int(raw_input())),
            4:lambda:numbersObject.display(),
            5:lambda:numbersObject.deleteFirst(),
            6:lambda:numbersObject.deleteAt(int(raw_input())),
            7:lambda:numbersObject.isEmpty(),
            8:lambda:numbersObject.length(),
            9:lambda:numbersObject.insertLast(int(raw_input())),
            10:lambda:exit(0)        
        }
    return options.get(value,lambda:"Value Doesn't Exist")();


def main():
    while True:
        print("Enter the Value : ");
        value = int(raw_input());
        switch(value);

if __name__ == '__main__':
    main();