'''
Created on 14-Dec-2017

@author: DELL
'''
from com.dst.sorting.BubbleSort import BubbleSort

class BinarySearch:
    
    def __init__(self,array):
        self.array = array;

    def search(self,element,left,right):
        position = -1;
        mid = (left+right)//2;
        if((element<self.array[mid]) and (left<right) and (right != mid)):
            position = self.search(element,left,mid);
        elif((element>self.array[mid]) and (left<right) and (left != mid)):
            position = self.search(element,mid,right);
        elif(element == self.array[mid]):
            return mid;
        return position;
    
    def set_array(self,array):
        self.array = array;

binary_search = BinarySearch([9,6,7,4,8,2,5,3,1]);
sort_array = BubbleSort(binary_search.array);
array = sort_array.sort();
binary_search.set_array(array);

def main():
    print(binary_search.search(3, 0, binary_search.array.__len__()-1));
    print(binary_search.search(11, 0, binary_search.array.__len__()-1));
    print(binary_search.search(3, 0, binary_search.array.__len__()-1));

if __name__ == '__main__':
    main();