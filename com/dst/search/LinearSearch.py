'''
Created on 14-Dec-2017

@author: DELL
'''

class LinearSearch:
    
    def __init__(self,array):
        self.array = array;
    
    def search(self,element):
        for i in range(0,self.array.__len__()):
            if(self.array[i] == element):
                return (i+1);
        return -1;

linear_search = LinearSearch([7,3,4,9,1,2,8,0,5,6]);

def main():
    print(linear_search.search(5));

if __name__ == '__main__':
    main();