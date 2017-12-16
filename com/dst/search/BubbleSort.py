'''
Created on 14-Dec-2017

@author: DELL
'''

class BubbleSort:
    '''
    classdocs
    '''


    def __init__(self, array):
        self.array = array;
    
    def sort(self):
        for i in range(0,self.array.__len__(),1):
            for j in range(0,self.array.__len__(),1):
                if(self.array[i]<self.array[j]):
                    x = self.array[i];
                    self.array[i] = self.array[j];
                    self.array[j] = x;
        return self.array;